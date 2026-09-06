"""
Funções e parâmetros compartilhados pelos scripts 02 a 05.

Concentra aqui tudo que a metodologia congela: composição dos grupos,
janelas de regime, regra de cobertura mínima e forma de calcular variação.
Mudar qualquer coisa neste arquivo muda todos os resultados, então toda
alteração precisa entrar no changelog público.
"""
import os
import pandas as pd, numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'data', 'raw')
PROC = os.path.join(ROOT, 'data', 'processed')
DOCS = os.path.join(ROOT, 'docs')
OUT = os.path.join(ROOT, 'outputs')

# Cobertura mínima, em anos observados no período, para um país entrar
# na mediana de um indicador esparso. Ver metodologia v3, seção 4.
MIN_OBS = 10

# Indicadores medidos por pesquisa amostral, sujeitos à regra acima.
ESPARSOS = {'SI.POV.DDAY', 'SI.POV.GINI', 'SI.POV.LMIC', 'DERIV.B40.SHARE',
            'SI.DST.10TH.10', 'SE.SEC.CUAT.UP.ZS'}

GRUPOS = {
    'America Latina':           ['MEX', 'COL', 'CHL', 'PER', 'ARG', 'ECU'],
    'G20 emergentes':           ['IND', 'IDN', 'ZAF', 'TUR', 'CHN', 'MEX'],
    'G20 emerg. sem China':     ['IND', 'IDN', 'ZAF', 'TUR', 'MEX'],
    'Exportadores commodities': ['CHL', 'COL', 'PER', 'ZAF', 'IDN'],
}

REGIMES = [('Boom de commodities', 2003, 2011),
           ('Desaceleração',       2012, 2014),
           ('Recessão e ajuste',   2015, 2018),
           ('Pandemia',            2019, 2021),
           ('Recuperação',         2022, 2025)]


def carrega_painel():
    """Lê o painel bruto e acrescenta a participação dos 40% mais pobres."""
    df = pd.read_csv(os.path.join(RAW, 'wb_raw.csv'))
    b40 = (df[df.indicador.isin(['SI.DST.FRST.20', 'SI.DST.02ND.20'])]
           .pivot_table(index=['iso', 'pais', 'ano'], columns='indicador', values='valor')
           .dropna())
    b40 = (b40.sum(axis=1).reset_index(name='valor')
           .assign(indicador='DERIV.B40.SHARE',
                   indicador_nome='Participacao de renda - 40% mais pobres'))
    return pd.concat([df, b40], ignore_index=True)


def serie(df, code, iso):
    """Série anual do indicador. Interpola linearmente APENAS dentro do
    intervalo observado, nunca extrapola. Ver limitação 2.4 da metodologia."""
    x = df[(df.indicador == code) & (df.iso == iso)].set_index('ano').valor.sort_index()
    x = x[~x.index.duplicated()]
    if len(x) < 2:
        return pd.Series(dtype=float)
    f = pd.Series(index=range(int(x.index.min()), int(x.index.max()) + 1), dtype=float)
    f.update(x)
    return f.interpolate()


def n_obs(df, code, iso, a=2002, b=2024):
    return df[(df.indicador == code) & (df.iso == iso)
              & (df.ano.between(a, b))].ano.nunique()


def grupo_filtrado(df, code, isos):
    """Aplica a regra de cobertura mínima aos indicadores esparsos."""
    if code not in ESPARSOS:
        return list(isos)
    return [i for i in isos if n_obs(df, code, i) >= MIN_OBS]


def variacao(s, a, b, tol_ini=2, tol_fim=2):
    """Variação entre as pontas da janela, em pontos e em proporção.

    A tolerância existe porque pesquisas domiciliares não caem exatamente
    nos anos da janela. Isso faz países usarem anos de ponta diferentes:
    é a limitação 2.3 da metodologia e precisa ser reportada por país.
    """
    if s.empty:
        return None
    ya = [y for y in s.index if a - 1 <= y <= a + tol_ini]
    yb = [y for y in s.index if b - tol_fim <= y <= b + 1]
    if not ya or not yb:
        return None
    ya, yb = min(ya), max(yb)
    if yb <= ya:
        return None
    return {'ini': s[ya], 'fim': s[yb], 'pp': s[yb] - s[ya],
            'rel': (s[yb] - s[ya]) / s[ya] * 100 if s[ya] else None,
            'ya': ya, 'yb': yb}


def mediana_grupo(df, code, isos, a, b, minimo=3, tol_ini=2, tol_fim=2):
    """Mediana das variações do grupo. Retorna None se faltar país.

    A tolerância PRECISA ser a mesma usada para o Brasil na mesma comparação,
    senão os dois lados usam anos de ponta diferentes e o diferencial fica
    contaminado. Passe sempre explicitamente.
    """
    v = [variacao(serie(df, code, i), a, b, tol_ini, tol_fim)
         for i in grupo_filtrado(df, code, isos)]
    v = [x for x in v if x]
    if len(v) < minimo:
        return None, len(v)
    rel = [x['rel'] for x in v if x['rel'] is not None]
    return {'pp': float(np.median([x['pp'] for x in v])),
            'rel': float(np.median(rel)) if rel else None,
            'ini': float(np.median([x['ini'] for x in v]))}, len(v)
