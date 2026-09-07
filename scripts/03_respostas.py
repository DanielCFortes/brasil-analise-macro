"""
03. Respostas às cinco perguntas e montagem do conjunto de dados da apresentação.

Entrada: data/processed/painel_final.csv
Saída:   data/processed/deck.json   séries dos gráficos, tabelas e respostas

Consolida tudo que a apresentação consome, para que o deck seja reprodutível
a partir do painel e não dependa de cálculo feito à mão.
"""
import os, json, pandas as pd, numpy as np
from comum import (PROC, RAW, MIN_OBS, carrega_painel, serie,
                   variacao, mediana_grupo, grupo_filtrado, n_obs)

LAC = ['MEX', 'COL', 'CHL', 'PER', 'ARG', 'ECU']
G20 = ['IND', 'IDN', 'ZAF', 'TUR', 'MEX']
EXP = ['CHL', 'COL', 'PER', 'ZAF', 'IDN']

NOMES = {'BRA': 'Brasil', 'MEX': 'México', 'COL': 'Colômbia', 'CHL': 'Chile',
         'PER': 'Peru', 'ARG': 'Argentina', 'ECU': 'Equador', 'IND': 'Índia',
         'IDN': 'Indonésia', 'ZAF': 'África do Sul', 'TUR': 'Turquia', 'CHN': 'China'}


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

    # --- séries dos gráficos: Brasil, América Latina e G20 sem China ---
    # Mesma base comparativa em todo indicador que tenha dado para os três.
    for chave, code in [('pov', 'SI.POV.DDAY'), ('gini', 'SI.POV.GINI'),
                        ('b40', 'DERIV.B40.SHARE'),
                        ('imr', 'SP.DYN.IMRT.IN'), ('san', 'SH.STA.BASS.ZS'),
                        ('hom', 'VC.IHR.PSRC.P5'), ('des', 'SL.UEM.TOTL.ZS')]:
        bra, lac, g20 = serie(df, code, 'BRA'), med_ano(df, code, LAC), med_ano(df, code, G20)
        D[chave] = {n: {y: (round(s[y], 2) if y in s.index and pd.notna(s[y]) else None)
                        for y in range(2002, 2027)}
                    for n, s in [('bra', bra), ('lac', lac), ('g20', g20)]}

    # --- índices com base 2002 = 100, mesma base comparativa ---
    def idx_grupo(code, isos, base=2002):
        """Mediana do índice (base 2002 = 100) entre os países do grupo.

        Cada país é indexado ao próprio valor de base antes da mediana,
        para não misturar nível com variação.
        """
        cols = {}
        for i in isos:
            s = serie(df, code, i)
            if base in s.index and pd.notna(s[base]) and s[base]:
                cols[i] = s / s[base] * 100
        if not cols:
            return pd.Series(dtype=float)
        return pd.DataFrame(cols).median(axis=1, skipna=True)

    D['idx'] = {}
    for chave, code in [('pib', 'NY.GDP.PCAP.PP.KD'), ('prod', 'SL.GDP.PCAP.EM.KD')]:
        bra = serie(df, code, 'BRA')
        bra_idx = bra / bra[2002] * 100
        lac_idx, g20_idx = idx_grupo(code, LAC), idx_grupo(code, G20)
        D['idx'][chave] = {n: {y: (round(s[y], 1) if y in s.index and pd.notna(s[y]) else None)
                               for y in range(2002, 2027)}
                           for n, s in [('bra', bra_idx), ('lac', lac_idx), ('g20', g20_idx)]}

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

    # --- crescimento contra diferentes conjuntos de pares ---
    # A escolha do grupo de comparação muda o veredito, então o deck publica todos
    # os grupos candidatos lado a lado em vez de escolher um e omitir os outros.
    # Pontas suavizadas por média de 3 anos: um ano de ponta atípico, de crise ou de
    # pico de commodity, não decide o resultado inteiro.
    BANDA = (0.75, 1.60)   # renda de 2000 relativa à do Brasil, congelada antes de olhar
    pib = df[df.indicador == 'NY.GDP.PCAP.PP.KD'].copy()
    pib['iso'] = pib['iso'].fillna('UMC')
    piv = pib.pivot_table(index='ano', columns='iso', values='valor')
    r_ini, r_fim = piv.loc[1999:2001].mean(), piv.loc[2023:2025].mean()
    cres = (r_fim / r_ini - 1) * 100

    paises = [i for i in cres.index if i != 'UMC']
    renda_br = r_ini['BRA']
    LARGADA = [i for i in paises if i != 'BRA'
               and renda_br * BANDA[0] <= r_ini[i] <= renda_br * BANDA[1]]

    def bloco(isos):
        isos = [i for i in isos if i in cres.index]
        return {'isos': isos, 'n': len(isos),
                'mediana': round(float(cres[isos].median()), 0),
                'dif': round(float(cres['BRA'] - cres[isos].median()), 0)}

    D['pares'] = {
        'banda': list(BANDA),
        'brasil': round(float(cres['BRA']), 0),
        'umc': round(float(cres['UMC']), 0),
        'paises': [{'iso': i, 'nome': NOMES[i],
                    'ini': round(float(r_ini[i]), 0), 'fim': round(float(r_fim[i]), 0),
                    'cresc': round(float(cres[i]), 0),
                    'largada': i in LARGADA or i == 'BRA'}
                   for i in sorted(paises, key=lambda x: -cres[x])],
        'grupos': [{'nome': 'América Latina', **bloco(LAC)},
                   {'nome': 'G20 emergentes sem China', **bloco(G20)},
                   {'nome': 'Exportadores de commodities', **bloco(EXP)},
                   {'nome': 'Largou perto do Brasil', **bloco(LARGADA)},
                   {'nome': 'Largou perto e exporta commodities',
                    **bloco([i for i in LARGADA if i in EXP])}],
    }

    # --- placar do Brasil contra os seis pares que largaram perto ---
    # Não é mediana de grupo: são os seis países, um a um. Duas leituras por
    # indicador, porque elas divergem: onde o Brasil ESTÁ (nível hoje) e para
    # onde o Brasil FOI (variação no período).
    PLACAR = [   # codigo, rotulo, bloco, maior_e_melhor, casas decimais
        ('NY.GDP.PCAP.PP.KD', 'PIB per capita (PPC)',        'eco', True,  0),
        ('SL.GDP.PCAP.EM.KD', 'Produtividade por ocupado',   'eco', True,  0),
        ('NE.GDI.TOTL.ZS',    'Investimento sobre PIB',      'eco', True,  1),
        ('NE.TRD.GNFS.ZS',    'Comércio sobre PIB',          'eco', True,  1),
        ('SL.UEM.TOTL.ZS',    'Desemprego',                  'eco', False, 1),
        ('FP.CPI.TOTL.ZG',    'Inflação',                    'eco', False, 1),
        ('GC.DOD.TOTL.GD.ZS', 'Dívida do governo central',   'eco', False, 1),
        ('SI.POV.DDAY',       'Pobreza extrema',             'soc', False, 1),
        ('SI.POV.GINI',       'Índice de Gini',              'soc', False, 1),
        ('DERIV.B40.SHARE',   'Renda dos 40% mais pobres',   'soc', True,  1),
        ('SP.DYN.IMRT.IN',    'Mortalidade infantil',        'soc', False, 1),
        ('SH.STA.BASS.ZS',    'Saneamento básico',           'soc', True,  1),
        ('SE.SEC.CUAT.UP.ZS', 'Ensino médio completo (25+)', 'soc', True,  1),
        ('SN.ITK.MSFI.ZS',    'Insegurança alimentar',       'soc', False, 1),
        ('VC.IHR.PSRC.P5',    'Homicídios',                  'soc', False, 1),
    ]
    SEIS = [i for i in LARGADA]                 # os seis pares da regra da largada
    TODOS = ['BRA'] + SEIS

    def ponta(s, a, b):
        w = s.loc[[y for y in s.index if a <= y <= b]].dropna()
        return float(w.mean()) if len(w) else None

    D['placar'] = {'pares': [NOMES[i] for i in SEIS], 'linhas': []}
    for code, rot, bloco, maior, dec in PLACAR:
        pv = df[df.indicador == code].pivot_table(index='ano', columns='iso', values='valor')
        ini = {i: ponta(pv[i].dropna(), 1999, 2003) for i in TODOS if i in pv.columns}
        fim = {i: ponta(pv[i].dropna(), 2021, 2025) for i in TODOS if i in pv.columns}
        ini = {k: v for k, v in ini.items() if v is not None}
        fim = {k: v for k, v in fim.items() if v is not None}
        if 'BRA' not in fim or len(fim) < 5:
            continue
        ordem = sorted(fim, key=lambda i: -fim[i] if maior else fim[i])
        linha = {'ind': rot, 'bloco': bloco, 'dec': dec,
                 'br': round(fim['BRA'], dec),
                 'rank_niv': ordem.index('BRA') + 1, 'n_niv': len(fim),
                 'melhor': NOMES[ordem[0]], 'rank_var': None, 'n_var': 0}
        comuns = [i for i in TODOS if i in ini and i in fim]
        if 'BRA' in comuns and len(comuns) >= 5:
            var = {i: fim[i] - ini[i] for i in comuns}
            ordem_v = sorted(var, key=lambda i: -var[i] if maior else var[i])
            linha.update({'rank_var': ordem_v.index('BRA') + 1, 'n_var': len(comuns)})
        D['placar']['linhas'].append(linha)

    # --- insegurança alimentar ---
    D['fome'] = {}
    for iso in ['BRA'] + LAC + ['IDN', 'ZAF']:
        s = df[(df.indicador == 'SN.ITK.MSFI.ZS') & (df.iso == iso)].set_index('ano').valor.sort_index()
        if len(s):
            D['fome'][iso] = {int(k): round(v, 1) for k, v in s.items()}
    lacf = pd.DataFrame({i: pd.Series(D['fome'][i]) for i in LAC if i in D['fome']})
    D['fome']['LAC_MED'] = {int(k): round(v, 1) for k, v in lacf.median(axis=1).items()}
    # G20 sem China: só Indonésia e África do Sul têm a série. Índia, Turquia
    # e China não têm dado FIES, então essa mediana é fraca e é rotulada como tal.
    g20f = pd.DataFrame({i: pd.Series(D['fome'][i]) for i in ['IDN', 'ZAF'] if i in D['fome']})
    D['fome']['G20_MED'] = {int(k): round(v, 1) for k, v in g20f.median(axis=1).items()}

    # --- Big Mac Index: evolutivo (preço em US$) e comparativo (valorização cambial) ---
    # Fonte: The Economist (github.com/TheEconomist/big-mac-data), licença aberta.
    # Extraído manualmente via GitHub em 06/09/2026, fora do pipeline automatizado:
    # a API do World Bank está bloqueada neste ambiente. Checkpoints discretos, não
    # série anual: 2002, 2012, 2018, 2020, 2022, 2025. Equador não tem série no Big
    # Mac Index (não entra na mediana da América Latina). Índia só entra a partir do
    # checkpoint de 2012, a série não cobre 2002.
    bm = pd.read_csv(os.path.join(RAW, 'bigmac_raw.csv'))
    D['bigmac'] = {}
    for metrica, col in [('preco', 'dollar_price'), ('valorizacao', 'val_pct')]:
        linhas = []
        for cp, g in bm.groupby('checkpoint'):
            bra = g.loc[g.iso == 'BRA', col]
            lac = g.loc[g.iso.isin([i for i in LAC if i != 'ECU']), col]
            grp20 = g.loc[g.iso.isin(G20), col]
            linhas.append({
                'checkpoint': int(cp),
                'bra': round(float(bra.iloc[0]), 2) if len(bra) else None,
                'lac': round(float(lac.median()), 2) if len(lac) else None,
                'lac_n': int(len(lac)),
                'g20': round(float(grp20.median()), 2) if len(grp20) else None,
                'g20_n': int(len(grp20)),
            })
        D['bigmac'][metrica] = sorted(linhas, key=lambda r: r['checkpoint'])

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
