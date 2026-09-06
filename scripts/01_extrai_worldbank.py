"""
01. Extração dos indicadores internacionais (Tier 1) da API do World Bank.

Saída:  data/raw/wb_raw.csv   painel bruto, uma linha por indicador/país/ano
        data/raw/wb_log.csv   log de cobertura por indicador

A base do World Bank é revisada periodicamente. Rodar de novo pode produzir
números diferentes dos versionados no repositório. Registre a data de extração.
"""
import os, requests, pandas as pd
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')

COUNTRIES = {
    'BRA': 'Brasil',
    'MEX': 'Mexico', 'COL': 'Colombia', 'CHL': 'Chile',
    'PER': 'Peru', 'ARG': 'Argentina', 'ECU': 'Equador',
    'IND': 'India', 'IDN': 'Indonesia', 'ZAF': 'Africa do Sul',
    'TUR': 'Turquia', 'CHN': 'China',
    'UMC': 'Upper middle income',
}

IND = {
    'NY.GDP.PCAP.PP.KD': 'PIB per capita PPC (const 2021 int$)',
    'NY.GDP.PCAP.KD':    'PIB per capita (const US$)',
    'NY.GDP.MKTP.KD.ZG': 'Crescimento do PIB (%)',
    'SL.GDP.PCAP.EM.KD': 'Produtividade (PIB por ocupado)',
    'NE.GDI.TOTL.ZS':    'Investimento / PIB (%)',
    'SL.UEM.TOTL.ZS':    'Desemprego (%, est. OIT)',
    'SL.EMP.VULN.ZS':    'Emprego vulneravel (%)',
    'SL.ISV.IFRM.ZS':    'Emprego informal (%)',
    'SI.POV.GINI':    'Indice de Gini',
    'SI.DST.FRST.20': 'Participacao de renda - 20% mais pobres',
    'SI.DST.02ND.20': 'Participacao de renda - 2o quintil',
    'SI.DST.10TH.10': 'Participacao de renda - 10% mais ricos',
    'SI.SPR.PC40.ZG': 'Crescimento anualizado renda bottom 40 (%)',
    'SI.SPR.PCAP.ZG': 'Crescimento anualizado renda media (%)',
    'SI.POV.DDAY':      'Pobreza extrema US$3,00 PPC 2021 (%)',
    'SI.POV.LMIC':      'Pobreza US$4,20 PPC 2021 (%)',
    'SI.POV.UMIC':      'Pobreza US$8,30 PPC 2021 (%)',
    'SP.DYN.IMRT.IN':   'Mortalidade infantil (por mil nasc.)',
    'SH.DYN.MORT':      'Mortalidade menores de 5 anos',
    'SH.STA.BASS.ZS':   'Saneamento basico (% pop.)',
    'SH.H2O.BASW.ZS':   'Agua potavel basica (% pop.)',
    'SH.IMM.IDPT':      'Cobertura vacinal DTP3 (%)',
    'SH.IMM.MEAS':      'Cobertura vacinal sarampo (%)',
    'SE.SEC.CUAT.UP.ZS':'Ensino medio completo (25+, %)',
    'SN.ITK.MSFI.ZS':   'Inseguranca alimentar moderada ou grave (%)',
    'per_allsp.cov_pop_tot': 'Cobertura de protecao social (%)',
    'VC.IHR.PSRC.P5':        'Homicidios (por 100 mil hab.)',
    'GC.DOD.TOTL.GD.ZS': 'Divida do governo central / PIB (%)',
    'FP.CPI.TOTL.ZG':    'Inflacao ao consumidor (%)',
    'NE.TRD.GNFS.ZS':    'Comercio / PIB (%)',
}

URL = ('https://api.worldbank.org/v2/country/' + ';'.join(COUNTRIES)
       + '/indicator/{i}?format=json&per_page=2000&date=1995:2026')


def pull(code):
    try:
        j = requests.get(URL.format(i=code), timeout=60).json()
    except Exception as e:
        return code, [], 'erro: ' + str(e)[:60]
    if not isinstance(j, list) or len(j) < 2 or not j[1]:
        return code, [], 'sem dados retornados'
    out = []
    for d in j[1]:
        if d['value'] is None:
            continue
        iso, nome = d['countryiso3code'], d['country']['value']
        if not iso:                       # agregados voltam sem codigo ISO
            iso = next((k for k, v in COUNTRIES.items() if v == nome), nome)
        out.append({'indicador': code, 'indicador_nome': IND[code], 'iso': iso,
                    'pais': COUNTRIES.get(iso, nome),
                    'ano': int(d['date']), 'valor': d['value']})
    return code, out, f'{len(out)} obs'


def main():
    os.makedirs(RAW, exist_ok=True)
    rows, log = [], []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for code, out, nota in ex.map(pull, list(IND)):
            rows += out
            log.append({'indicador': code, 'nome': IND[code], 'obs': len(out), 'nota': nota})
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RAW, 'wb_raw.csv'), index=False)
    pd.DataFrame(log).to_csv(os.path.join(RAW, 'wb_log.csv'), index=False)
    print('linhas:', len(df), '| indicadores com dado:', df.indicador.nunique(), 'de', len(IND))
    vazios = [l['indicador'] for l in log if l['obs'] == 0]
    if vazios:
        print('sem dado:', ', '.join(vazios))


if __name__ == '__main__':
    main()
