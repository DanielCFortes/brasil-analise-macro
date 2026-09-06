"""
02. Desempenho diferencial por regime econômico.

Entrada: data/raw/wb_raw.csv
Saída:   data/processed/painel_final.csv         painel com indicadores derivados
         data/processed/resultados_diferencial.csv
         data/processed/cobertura.csv            anos observados por país/indicador

Publica sempre as duas medidas de variação, pontos percentuais e proporcional.
Nenhuma sozinha sustenta conclusão. Ver relatório de limitações, seção 7.1.
"""
import os, pandas as pd
from comum import (PROC, GRUPOS, REGIMES, carrega_painel, serie,
                   variacao, mediana_grupo, n_obs)

HEAD = ['NY.GDP.PCAP.PP.KD', 'SL.GDP.PCAP.EM.KD', 'SI.POV.DDAY', 'SI.POV.LMIC',
        'SI.POV.GINI', 'DERIV.B40.SHARE', 'SI.DST.10TH.10', 'SP.DYN.IMRT.IN',
        'SH.STA.BASS.ZS', 'VC.IHR.PSRC.P5', 'SL.UEM.TOTL.ZS', 'SL.EMP.VULN.ZS',
        'SE.SEC.CUAT.UP.ZS']


def main():
    os.makedirs(PROC, exist_ok=True)
    df = carrega_painel()
    out, cov = [], []
    for code in HEAD:
        sub = df[df.indicador == code]
        if sub.empty:
            continue
        nome = sub.indicador_nome.iloc[0]
        for rnome, a, b in REGIMES:
            br = variacao(serie(df, code, 'BRA'), a, b)
            row = {'indicador': nome, 'regime': rnome, 'janela': f'{a}-{b}',
                   'anos_brasil': f"{br['ya']}-{br['yb']}" if br else None,
                   'delta_brasil': round(br['pp'], 2) if br else None,
                   'rel_brasil': round(br['rel'], 1) if br and br['rel'] is not None else None}
            for gnome, isos in GRUPOS.items():
                m, n = mediana_grupo(df, code, isos, a, b)
                row[f'n_{gnome}'] = n
                row[f'delta_{gnome}'] = round(m['pp'], 2) if m else None
                row[f'rel_{gnome}'] = round(m['rel'], 1) if m and m['rel'] is not None else None
                row[f'dif_{gnome}'] = round(br['pp'] - m['pp'], 2) if (m and br) else None
            out.append(row)
        for iso in ['BRA'] + sorted({i for v in GRUPOS.values() for i in v}) + ['UMC']:
            s = df[(df.indicador == code) & (df.iso == iso) & (df.ano.between(2002, 2026))]
            cov.append({'indicador': nome, 'iso': iso, 'obs_reais': len(s),
                        'obs_2002_2024': n_obs(df, code, iso),
                        'primeiro': s.ano.min() if len(s) else None,
                        'ultimo': s.ano.max() if len(s) else None})

    df.to_csv(os.path.join(PROC, 'painel_final.csv'), index=False)
    pd.DataFrame(out).to_csv(os.path.join(PROC, 'resultados_diferencial.csv'), index=False)
    pd.DataFrame(cov).drop_duplicates().to_csv(os.path.join(PROC, 'cobertura.csv'), index=False)
    print('painel:', len(df), 'linhas | resultados:', len(out), '| cobertura:', len(cov))


if __name__ == '__main__':
    main()
