# Análise socioeconômica e de direitos: Brasil, 2002 a 2026

`github.com/DanielCFortes/brasil-analise-macro`

Avaliação da evolução do crescimento econômico, do bem estar, da desigualdade e das garantias de direitos no Brasil ao longo de 24 anos, com comparação internacional explícita contra grupos de países emergentes.

**Status: em andamento.** A especificação metodológica está congelada na v3. A extração internacional está parcial. A extração nacional não começou. Nenhuma conclusão deste repositório deve ser tratada como final.

---

## O que já existe

| Etapa | Situação |
| :--- | :--- |
| Especificação metodológica | Concluída, v3.0 |
| Extração internacional (Tier 1) | Parcial: 29 de 30 indicadores do World Bank, 8.732 observações |
| Extração nacional (Tier 2) | Não iniciada |
| Análise e publicação | Bloqueada por cinco decisões metodológicas abertas |

Respostas preliminares às cinco perguntas do projeto estão em `docs/apresentacao.html`, slides 15 a 19. São preliminares porque não há desagregação, não há dado tributário de topo e a pergunta transversal sobre custo fiscal segue sem resposta.

---

## Estrutura

```
metodologia/
  metodologia-v3.md     especificação vigente, congelar antes de extrair
  metodologia-v2.md     versão anterior, mantida para histórico
scripts/
  comum.py                     grupos, regimes, regra de cobertura e cálculo de variação
  01_extrai_worldbank.py       extração da API do World Bank
  02_desempenho_diferencial.py deltas por regime, Brasil contra medianas
  03_respostas.py              respostas às cinco perguntas e dados da apresentação
  04_monta_planilha.py         gera a planilha de entrega
  05_monta_apresentacao.py     gera a apresentação HTML
data/
  raw/         resposta bruta da API, sem tratamento
  processed/   painel consolidado, resultados e matriz de cobertura
docs/
  apresentacao.html                   apresentação de 26 slides, abre no navegador
  relatorio-extracao-limitacoes.md    o que foi extraído, o que falta e o que quebrou
outputs/
  extracao_brasil_2002_2026.xlsx      planilha com painel, resultados e cobertura
```

---

## Reproduzir

```bash
pip install -r requirements.txt
cd scripts
python 01_extrai_worldbank.py
python 02_desempenho_diferencial.py
python 03_respostas.py
python 04_monta_planilha.py
python 05_monta_apresentacao.py
```

Todos os caminhos são relativos à raiz do repositório. Rode de dentro de `scripts/`, que é onde o `comum.py` é importado.

Os parâmetros que a metodologia congela (composição dos grupos, janelas de regime, cobertura mínima e forma de calcular variação) estão todos em `scripts/comum.py`. Alterar esse arquivo muda todos os resultados e exige entrada no changelog público.

A extração vai à internet e leva alguns minutos. A base do World Bank é atualizada periodicamente, então rodar de novo pode produzir números diferentes dos que estão em `data/`. A data de extração dos dados versionados aqui é **06/09/2026**, sobre a base atualizada em **13/07/2026**.

---

## Desenho analítico, em resumo

A métrica principal é **desempenho diferencial**: a variação do Brasil menos a variação da mediana do grupo de comparação. Não é um contrafactual causal, e a especificação declara isso explicitamente.

Toda variação é publicada em duas medidas obrigatórias e simultâneas: **pontos percentuais e redução proporcional**. A razão está documentada em `docs/relatorio-extracao-limitacoes.md`, seção 7.1: variação em pontos percentuais não é comparável entre países com níveis iniciais muito diferentes, e usar só ela produziu uma conclusão errada em uma versão anterior.

Grupos de comparação: América Latina, G20 emergentes (sempre com e sem China), emergentes amplo e exportadores líquidos de commodities. **Regra de cobertura:** um país só entra na mediana de um indicador esparso se tiver ao menos 10 anos observados no período. Índia (4 anos) e África do Sul (5 anos) ficam fora dos indicadores de distribuição por essa regra. A exclusão alterou o resultado do boom de commodities e por isso as duas versões precisam ser publicadas lado a lado.

Mandatos presidenciais são camada narrativa, não unidade de cálculo. A análise não atribui resultado a governos.

---

## Limitações conhecidas

Quatro pontos quebram a especificação atual e exigem decisão antes de prosseguir:

1. A regra de não interpolar 2020 conflita com a fonte: o World Bank PIP tem pobreza e Gini do Brasil em 2020, derivados de fonte alternativa. E 2010 está ausente, por ser ano censitário.
2. Cobertura de distribuição assimétrica entre países, tratada pela regra dos 10 anos mas ainda desigual.
3. As janelas de regime não foram respeitadas no cálculo: a janela nominal de 2003 a 2011 virou 2002 a 2012 para o Brasil, e países diferentes usam anos de ponta diferentes.
4. Interpolação linear em série de pesquisa amostral suaviza reversões reais.

Sem dado: informalidade, prosperidade compartilhada como série anual, insegurança alimentar antes de 2015, cobertura de proteção social, dívida sobre PIB para quatro países.

Não extraído: WID.world, V-Dem, ITUC, UNODC direto, World Prison Brief, IMF WEO, OMS, e **todo o Tier 2 nacional**, que é onde está a desagregação por raça, região, gênero e situação do domicílio.

O relatório completo está em `docs/relatorio-extracao-limitacoes.md`.

---

## Decisões abertas

0. Adotar pontos percentuais e redução proporcional sempre juntos, revisando os resultados já calculados
1. 2020: aceitar o valor do PIP declarando a origem, ou remover o ponto
2. Interpolação: manter com declaração, ou comparar só anos observados nos dois lados
3. Janelas: tolerância zero, ou registrar por país os anos usados
4. Informalidade: download manual do ILOSTAT, ou PNAD Contínua quebrando a regra de não mistura
5. G20 emergentes em distribuição: grupo secundário, ou manter com aviso de cobertura em cada gráfico

---

## Fontes

World Bank (WDI e PIP) para todos os dados atualmente no repositório. As demais fontes previstas na metodologia estão listadas em `metodologia/metodologia-v3.md`, seção 3.

Dados públicos. Código e dados brutos publicados junto com os resultados, conforme o protocolo de reprodutibilidade da seção 13 da metodologia.
