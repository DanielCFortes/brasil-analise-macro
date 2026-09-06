"""
03. Respostas às cinco perguntas e montagem do conjunto de dados da apresentação.

Entrada: data/processed/painel_final.csv
Saída:   data/processed/deck.json   séries dos gráficos, tabelas e respostas

Consolida tudo que a apresentação consome, para que o deck seja reprodutível
a partir do painel e não dependa de cálculo feito à mão.
"""
import os, json, pandas as pd, numpy as np
from comum import (PROC, REGIMES, MIN_OBS, carrega_painel, serie,
                   variacao, mediana_grupo, grupo_filtrado, n_obs)

LAC = ['MEX', 'COL', 'CHL', 'PER', 'ARG', 'ECU']
G20 = ['IND', 'IDN', 'ZAF', 'TUR', 'MEX']
EXP = ['CHL', 'COL', 'PER', 'ZAF', 'IDN']

NOMES = {'BRA': 'Brasil', 'MEX': 'Mexico', 'COL': 'Colombia', 'CHL': 'Chile',
         'PER': 'Peru', 'ARG': 'Argentina', 'ECU': 'Equador', 'IND': 'India',
         'IDN': 'Indonesia', 'ZAF': 'Africa do Sul', 'TUR': 'Turquia', 'CHN': 'China'}

# pergunta, codigo, rotulo, unidade, casas decimais
IND_RESP = [
 ('P1', 'NY.GDP.PCAP.PP.KD', 'PIB per capita (PPC 2021, int$)', 'int$', 0),
 ('P1', 'SL.GDP.PCAP.EM.KD', 'Produtividade (PIB por ocupado)', 'int$', 0),
 ('P1', 'NE.GDI.TOTL.ZS',    'Investimento sobre PIB', '%', 1),
 ('P1', 'SL.UEM.TOTL.ZS',    'Desemprego', '%', 1),
 ('P2', 'SI.POV.GINI',       'Índice de Gini', 'pts', 1),
 ('P2', 'DERIV.B40.SHARE',   'Participação dos 40% mais pobres', '%', 1),
 ('P2', 'SI.DST.10TH.10',    'Participação dos 10% mais ricos', '%', 1),
 ('P3', 'SI.POV.DDAY',       'Pobreza extrema (US$ 3,00)', '%', 1),
 ('P3', 'SI.POV.LMIC',       'Pobreza (US$ 4,20)', '%', 1),
 ('P3', 'SP.DYN.IMRT.IN',    'Mortalidade infantil', 'por mil', 1),
 ('P3', 'SH.STA.BASS.ZS',    'Saneamento básico', '%', 1),
 ('P3', 'SN.ITK.MSFI.ZS',    'Insegurança alimentar', '%', 1),
 ('P3', 'SE.SEC.CUAT.UP.ZS', 'Ensino médio completo (25+)', '%', 1),
 ('P4b','VC.IHR.PSRC.P5',    'Homicídios', 'por 100 mil', 1),
]


def med_ano(df, code, isos):
    """Mediana ano a ano do grupo, para as linhas dos gráficos."""
    d = pd.DataFrame({i: serie(df, code, i) for i in grupo_filtrado(df, code, isos)})
    return d.median(axis=1, skipna=True)


def main():
    df = carrega_painel()
    D = {}

    # --- séries dos gráficos: Brasil e medianas ---
    for chave, code in [('pov', 'SI.POV.DDAY'), ('gini', 'SI.POV.GINI'),
                        ('b40', 'DERIV.B40.SHARE')]:
        bra, lac, g20 = serie(df, code, 'BRA'), med_ano(df, code, LAC), med_ano(df, code, G20)
        D[chave] = {n: {y: (round(s[y], 2) if y in s.index and pd.notna(s[y]) else None)
                        for y in range(2002, 2025)}
                    for n, s in [('bra', bra), ('lac', lac), ('g20', g20)]}

    # --- índices com base 2002 = 100 ---
    D['idx'] = {}
    for chave, code in [('pib', 'NY.GDP.PCAP.PP.KD'), ('prod', 'SL.GDP.PCAP.EM.KD')]:
        s = serie(df, code, 'BRA')
        D['idx'][chave] = {y: round(s[y] / s[2002] * 100, 1)
                           for y in range(2002, 2026) if y in s.index}

    # --- indicadores sociais do Brasil ---
    D['soc'] = {}
    for chave, code in [('imr', 'SP.DYN.IMRT.IN'), ('san', 'SH.STA.BASS.ZS'),
                        ('hom', 'VC.IHR.PSRC.P5'), ('des', 'SL.UEM.TOTL.ZS')]:
        s = serie(df, code, 'BRA')
        D['soc'][chave] = {y: round(s[y], 1) for y in range(2002, 2026) if y in s.index}

    # --- grade de disponibilidade: anos OBSERVADOS, sem interpolação ---
    D['grid'] = []
    for iso, nome in NOMES.items():
        anos = set(df[(df.indicador == 'SI.POV.GINI') & (df.iso == iso)].ano)
        marca = [1 if y in anos else 0 for y in range(2002, 2025)]
        D['grid'].append({'pais': nome, 'anos': marca, 'n': sum(marca)})

    # --- tabela de pobreza por regime, nas duas medidas ---
    D['tab2'] = []
    for nome, a, b in REGIMES:
        br = variacao(serie(df, 'SI.POV.DDAY', 'BRA'), a, b)
        r = {'reg': nome, 'br_ini': round(br['ini'], 1),
             'br_pp': round(br['pp'], 1), 'br_rel': round(br['rel'], 0)}
        for g, isos in [('lac', LAC), ('g20', G20), ('exp', EXP)]:
            m, n = mediana_grupo(df, 'SI.POV.DDAY', isos, a, b)
            r[g + '_n'] = n
            r[g + '_pp'] = round(m['pp'], 1) if m else None
            r[g + '_rel'] = round(m['rel'], 0) if m else None
        D['tab2'].append(r)

    # --- respostas às cinco perguntas: 2002 contra o último ano disponível ---
    D['ans'] = []
    for q, code, rotulo, unid, dec in IND_RESP:
        a, b = (2015, 2023) if code == 'SN.ITK.MSFI.ZS' else (2002, 2025)
        TOL = 3   # mesma tolerancia dos dois lados da comparacao
        br = variacao(serie(df, code, 'BRA'), a, b, tol_ini=TOL, tol_fim=TOL)
        if not br:
            continue
        r = {'q': q, 'ind': rotulo, 'unid': unid,
             'br_ini': round(br['ini'], dec), 'br_fim': round(br['fim'], dec),
             'br_pp': round(br['pp'], dec),
             'br_rel': round(br['rel'], 0) if br['rel'] is not None else None,
             'anos': f"{br['ya']}-{br['yb']}"}
        for g, isos in [('lac', LAC), ('g20', G20)]:
            m, n = mediana_grupo(df, code, isos, a, b, tol_ini=TOL, tol_fim=TOL)
            r[g + '_n'] = n
            r[g + '_pp'] = round(m['pp'], dec) if m else None
            r[g + '_rel'] = round(m['rel'], 0) if m and m['rel'] is not None else None
        D['ans'].append(r)

    # --- insegurança alimentar ---
    D['fome'] = {}
    for iso in ['BRA'] + LAC + ['IDN', 'ZAF']:
        s = df[(df.indicador == 'SN.ITK.MSFI.ZS') & (df.iso == iso)].set_index('ano').valor.sort_index()
        if len(s):
            D['fome'][iso] = {int(k): round(v, 1) for k, v in s.items()}
    lacf = pd.DataFrame({i: pd.Series(D['fome'][i]) for i in LAC if i in D['fome']})
    D['fome']['LAC_MED'] = {int(k): round(v, 1) for k, v in lacf.median(axis=1).items()}

    # --- efeito da regra de cobertura sobre o resultado do boom ---
    todos = [variacao(serie(df, 'SI.POV.DDAY', i), 2003, 2011) for i in G20]
    todos = [x for x in todos if x]
    com_regra, n = mediana_grupo(df, 'SI.POV.DDAY', G20, 2003, 2011)
    D['regra'] = {
        'min_obs': MIN_OBS,
        'excluidos': [[i, int(n_obs(df, 'SI.POV.DDAY', i))]
                      for i in set(LAC + G20 + EXP) if n_obs(df, 'SI.POV.DDAY', i) < MIN_OBS],
        'boom_sem_regra': round(float(np.median([x['pp'] for x in todos])), 1),
        'boom_com_regra': round(com_regra['pp'], 1) if com_regra else None,
    }

    with open(os.path.join(PROC, 'deck.json'), 'w') as f:
        json.dump(D, f)
    print('deck.json escrito |', len(D['ans']), 'indicadores respondidos')
    print('regra de cobertura, excluídos:', D['regra']['excluidos'])
    print('boom sem regra:', D['regra']['boom_sem_regra'],
          '| com regra:', D['regra']['boom_com_regra'])


if __name__ == '__main__':
    main()
