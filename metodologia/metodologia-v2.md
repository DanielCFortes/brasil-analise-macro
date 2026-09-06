# Metodologia de Análise Socioeconômica e de Direitos: Brasil (2002 a 2026)

**Versão 2.0 | Documento público de especificação metodológica**

Este documento define o framework metodológico, conceitual e operacional para analisar a evolução do bem estar, da desigualdade e das garantias de direitos das populações de baixa renda no Brasil entre 2002 e 2026, com contrafactual internacional explícito.

Por ser destinado a publicação, o documento declara antecipadamente o desenho de identificação, os testes de robustez obrigatórios e os limites do que a análise pode concluir. A especificação é congelada antes da coleta de dados.

---

## 1. Objetivo e Escopo

**Objetivo:** medir a evolução do bem estar e dos direitos da base da pirâmide social brasileira e estimar quanto dessa evolução é atribuível a condições domésticas versus tendências globais compartilhadas.

**Período:** 2002 a 2026. O ciclo 2023 a 2026 está incompleto na data de publicação e é reportado como parcial.

**Recorte populacional:** foco nos 40% de menor rendimento, com desagregação obrigatória por região, raça e gênero.

**Duas perguntas distintas, reportadas separadamente:**

| Pergunta | Tipo | O que responde |
| :--- | :--- | :--- |
| O que aconteceu com a base da pirâmide? | Descritiva | Trajetória absoluta dos indicadores |
| Quanto disso foi específico do Brasil? | Comparativa | Desempenho relativo ao grupo de controle |

A análise **não** responde qual política causou qual resultado. Ver seção 9.

---

## 2. Desenho de Identificação

Esta é a seção que sustenta a credibilidade da análise. Todo resultado publicado passa por ela.

### 2.1 Contrafactual: o delta relativo é a métrica principal

Variação absoluta de um indicador no Brasil não é resultado. O resultado reportado é:

> **Delta relativo = (variação do Brasil no período) menos (variação da mediana do grupo de controle no mesmo período)**

Se a pobreza extrema cai 8 pontos no Brasil e 7 pontos na mediana dos emergentes, o desempenho relativo é de 1 ponto, não de 8. Ambos os números são publicados, sempre lado a lado.

**Hipótese assumida:** tendências paralelas. Os choques globais afetaram os países do grupo de controle de forma diferente em magnitude, mas na média o efeito é tratado como comum. Esta hipótese é declarada como limitação e testada no ponto 2.4.

### 2.2 Métrica secundária: posição percentílica

Além do delta, reporta se o **percentil do Brasil dentro do grupo de controle** em cada ano. Essa métrica é imune à composição do grupo e responde diretamente: o Brasil melhorou, ou apenas acompanhou a melhora geral?

### 2.3 Três camadas temporais sobre a mesma série

A série anual é a unidade de análise. Os agrupamentos são camadas de leitura, não unidades de medida.

**Camada A. Série anual contínua.** Base de todos os gráficos, com eventos marcados como linhas verticais.

**Camada B. Regimes econômicos.** Períodos definidos por condições externas, não por calendário político:

| Regime | Anos |
| :--- | :--- |
| Boom de commodities | 2003 a 2011 |
| Desaceleração pós boom | 2012 a 2014 |
| Recessão e ajuste | 2015 a 2018 |
| Pandemia | 2020 a 2021 |
| Recuperação | 2022 a 2026 |

**Camada C. Mandatos presidenciais, com defasagem de 1 ano.** O mandato iniciado em 2003 é avaliado sobre o intervalo 2004 a 2007, e assim por diante. Política pública leva tempo para aparecer no indicador.

**Regra de robustez:** o delta é calculado nas camadas B e C. Convergência entre as duas indica achado robusto. **Divergência entre as duas é reportada como resultado, não resolvida por escolha do autor.**

### 2.4 Testes de robustez obrigatórios

**Teste 1. Termos de troca (commodities).** O boom de 2003 a 2011 não afetou os pares de forma homogênea. Brasil, Chile, Colômbia e África do Sul são exportadores líquidos de commodities. México, Índia e Turquia não são. O ganho brasileiro no período é recalculado contra o subgrupo de exportadores. Se a vantagem desaparecer nessa comparação, a conclusão do período é revista.

**Teste 2. Sensibilidade à composição do grupo.** Cada resultado é recalculado com e sem China no agregado G20 emergentes, e com exclusão sequencial de cada país do agregado latino americano. Resultados que invertem sinal com a saída de um único país são marcados como frágeis.

**Teste 3. Sensibilidade ao recorte temporal.** Deslocamento das janelas em mais ou menos 1 ano. Achados que só existem em um recorte específico não são publicados como conclusão.

### 2.5 Exceção declarada: pandemia

O choque da COVID-19 é global, mas a **magnitude da resposta fiscal foi escolha doméstica**. A resposta emergencial de transferência de renda em percentual do PIB não é neutralizada pelo contrafactual. Neste caso, a diferença contra os pares é o objeto de medição, não ruído a ser removido.

---

## 3. Arquitetura de Dados

### 3.1 Dois tiers, sem mistura

**Tier 1. Comparação internacional.** Exclusivamente bases já harmonizadas entre países. Nenhuma fonte nacional entra neste tier, **inclusive para o Brasil**.

| Domínio | Base |
| :--- | :--- |
| Pobreza, Gini, renda dos 40% mais pobres | World Bank PIP |
| Emprego, informalidade, subutilização, previdência | ILOSTAT |
| Desenvolvimento humano e IDH-D | UNDP |
| Saneamento | JMP (WHO / UNICEF) |
| Educação | UNESCO UIS |
| Homicídios | UNODC |
| Insegurança alimentar | FAO SOFI (escala FIES) |
| Concentração de renda no topo | WID.world |
| Mortalidade infantil | UN IGME |
| Cobertura vacinal | WHO WUENIC |
| Fiscal | IMF WEO |
| Direitos do trabalho | ITUC Global Rights Index |
| Institucional | V-Dem |

**Tier 2. Brasil em alta resolução.** IBGE, DataSUS, INEP, SNIS, CadÚnico, BCB, FBSP, Tesouro, Receita Federal, MTE. É neste tier que ocorre toda a desagregação.

### 3.2 Regra de não mistura

O valor do Brasil em qualquer gráfico comparativo vem do Tier 1, mesmo quando difere do valor oficial do IBGE. As duas séries divergem por definição metodológica. A divergência é documentada uma vez, em nota técnica, e não é reconciliada.

### 3.3 Estrutura de apresentação

1. Brasil agregado, com Tier 1 e Tier 2 lado a lado
2. Brasil desagregado, apenas Tier 2
3. Brasil contra benchmarks, apenas Tier 1

---

## 4. Grupo de Controle

Três agregados independentes, calculados por **mediana** (não média, para evitar dominância de outliers). Composição congelada no início da análise e não alterada após a visualização dos resultados.

| Agregado | Composição |
| :--- | :--- |
| América Latina | México, Colômbia, Chile, Peru, Argentina, Equador |
| G20 emergentes | Índia, Indonésia, África do Sul, Turquia, México, China |
| Emergentes amplo | Agregado "upper middle income" do Banco Mundial |

Todo resultado do agregado G20 emergentes é reportado com e sem China.

**Ajustes monetários:** todas as comparações de renda e pobreza em US$ PPC, usando as PPCs de 2021. A linha internacional de pobreza extrema vigente é **US$ 3,00 por dia em PPC de 2021**, revisada pelo Banco Mundial em junho de 2025. A série histórica é baixada já recalculada do World Bank PIP. Nenhuma conversão manual é realizada.

---

## 5. Matriz de Indicadores

### Pilar Econômico

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Renda real dos 40% mais pobres | Headline | PNAD Contínua | World Bank PIP |
| Taxa de informalidade | Headline | PNAD Contínua | ILOSTAT |
| Participação do 1% mais rico | Headline | DIRPF / Receita | WID.world |
| Taxa de subutilização da força de trabalho | Suporte | PNAD Contínua | ILOSTAT |
| Salário mínimo real | Suporte | MTE / IPEA | sem equivalente |
| Percentual da força de trabalho no piso | Suporte | PNAD Contínua | sem equivalente |
| Comprometimento de renda com dívida | Suporte | BCB / PEIC | sem equivalente |

O indicador de salário mínimo é lido junto ao percentual da força de trabalho que recebe o piso e à indexação de aposentadorias e BPC, que são os canais efetivos de transmissão.

### Pilar Social

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Taxa de extrema pobreza | Headline | IBGE | World Bank PIP |
| Insegurança alimentar | Headline | PENSSAN / POF | FAO SOFI (FIES) |
| Mortalidade infantil | Headline | DataSUS | UN IGME |
| Acesso a saneamento | Suporte | PNAD Contínua, calibrada por Censo | JMP |
| Conclusão do ensino médio (18 a 24 anos) | Suporte | INEP / IBGE | UNESCO UIS |
| Cobertura vacinal | Suporte | PNI / DataSUS | WHO WUENIC |

### Pilar Direitos

Reestruturado em três dimensões. A versão anterior continha apenas cobertura de proteção social, que é dimensão social e não de direitos.

**Proteção social**

| Indicador | Fonte BR | Fonte internacional |
| :--- | :--- | :--- |
| Cobertura previdenciária | INSS / PNAD | ILOSTAT |
| Cobertura de transferência de renda | MDS / CadÚnico | ILO Social Protection |

**Direitos do trabalho**

| Indicador | Fonte BR | Fonte internacional |
| :--- | :--- | :--- |
| Autos de infração e fiscalização trabalhista | MTE | sem equivalente |
| Resgates de trabalho análogo à escravidão | MTE | sem equivalente |
| Índice de direitos sindicais e trabalhistas | não aplicável | ITUC Global Rights Index |

**Direitos civis e violência**

| Indicador | Fonte BR | Fonte internacional |
| :--- | :--- | :--- |
| Taxa de homicídios | SIM / DataSUS | UNODC |
| Mortes por causa indeterminada | SIM / DataSUS | não aplicável |
| Mortes por intervenção policial | FBSP | não aplicável |
| Taxa de encarceramento | SISDEPEN | World Prison Brief |
| Índice de democracia igualitária | não aplicável | V-Dem |

**Protocolo de homicídios.** A série principal do Brasil é SIM/DataSUS (mortes por agressão), por ser registro de saúde e menos sujeito a incentivo de classificação policial. A série de mortes por causa indeterminada é publicada **sempre ao lado**, porque em alguns estados absorve homicídios reclassificados. O FBSP entra como fonte secundária por separar mortes por intervenção policial. Comparações internacionais usam exclusivamente UNODC.

### Camada Fiscal (transversal)

Não é pilar. Roda por baixo dos três e responde uma pergunta única: o ganho de bem estar do período foi financiado ou antecipado do período seguinte.

| Indicador | Fonte BR | Fonte internacional |
| :--- | :--- | :--- |
| Dívida bruta sobre PIB | Tesouro / BCB | IMF WEO |
| Resultado primário | Tesouro | IMF WEO |
| Gasto social sobre PIB | Tesouro / SIOP | IMF / ILO |

---

## 6. Desagregação Obrigatória

Média nacional oculta trajetórias divergentes. Todo indicador headline do Tier 2 é publicado desagregado por:

* **Região:** cinco macrorregiões, com destaque Nordeste versus Sudeste
* **Raça e cor:** classificação IBGE
* **Gênero**
* **Situação do domicílio:** urbano e rural

Indicadores de suporte são desagregados quando a fonte permitir. Ausência de desagregação é declarada, não omitida.

---

## 7. Quebras Metodológicas e Lacunas

| Situação | Tratamento |
| :--- | :--- |
| PNAD antiga (até 2011) e PNAD Contínua (a partir de 2012) | Séries reportadas separadamente, com marcador de quebra. Sem encadeamento retroativo. |
| 2020, suspensão da coleta presencial da PNAD Contínua anual | Não interpolar. PNAD COVID usada apenas para direção, nunca para nível. Comparações ancoradas em 2019 e 2021. |
| Censo 2010 e 2022, sem Censo 2020 | Suplemento anual da PNAD Contínua como série contínua; Censos usados apenas para calibração de nível. |
| CadÚnico | Reclassificado. Deixa de ser proxy de pobreza e passa a ser indicador próprio de cobertura e focalização. Aumento de cobertura pode indicar mais pobreza ou mais busca ativa, e a análise não separa os dois efeitos. |
| Linha internacional de pobreza | US$ 3,00 em PPC de 2021. Série baixada já recalculada do PIP. |
| Inflação da base | INPC (cesta de 1 a 5 salários mínimos) para custo de vida real dos estratos inferiores. IPCA usado apenas quando exigido por comparabilidade internacional. |

**Regra visual:** nenhum gráfico exibe linha contínua atravessando quebra metodológica. Toda quebra é marcada.

---

## 8. Cronologia de Referência

Tabela de eventos verificáveis, sem interpretação. A caracterização de cada período é escrita **após** a análise dos dados, não antes.

| Ciclo | Mandato | Janela avaliada (lag 1) | Eventos verificáveis |
| :---: | :---: | :---: | :--- |
| I | 2003 a 2006 | 2004 a 2007 | Unificação do Bolsa Família; início da regra de valorização do salário mínimo; alta do índice de preços de commodities |
| II | 2007 a 2010 | 2008 a 2011 | Crise financeira global de 2008; PAC; expansão do crédito consignado |
| III | 2011 a 2014 | 2012 a 2015 | Transição para PNAD Contínua; queda do índice de preços de commodities a partir de 2011 |
| IV | 2015 a 2018 | 2016 a 2019 | Recessão de 2015 e 2016; impeachment; Emenda do Teto de Gastos; Reforma Trabalhista |
| V | 2019 a 2022 | 2020 a 2023 | Reforma da Previdência; pandemia de COVID-19; Auxílio Emergencial; Novo Marco do Saneamento; choque inflacionário global |
| VI | 2023 a 2026 | 2024 a 2026 (parcial) | Recomposição do Bolsa Família; novo arcabouço fiscal; Reforma Tributária do consumo |

---

## 9. Validação Macro

Aplicados ao final da série de 24 anos, para verificar coerência com os indicadores anuais:

1. **IDH-D:** perda de desenvolvimento humano provocada pela desigualdade em renda, educação e saúde
2. **IPS (Índice de Progresso Social):** qualidade de vida sem neutralização pelo PIB
3. **Índice de Gini:** trajetória da distribuição de renda domiciliar

Os três são reportados também no formato de delta relativo contra os agregados de controle.

**Nota sobre o Gini:** pesquisas domiciliares subestimam sistematicamente a renda do topo. O Gini é sempre publicado ao lado da participação do 1% mais rico apurada por dados tributários (WID.world). Gini em queda com concentração no topo estável é um resultado possível e não deve ser apresentado como contradição.

---

## 10. Limitações Declaradas

Declaradas antes da coleta, não após.

1. **A análise não estabelece causalidade entre política específica e resultado.** Ela mede desempenho relativo em janelas temporais. Atribuição de crédito ou culpa a governos individuais está fora do escopo.
2. **A hipótese de tendências paralelas pode falhar.** É testada apenas para o canal de commodities e composição do grupo. Outros canais assimétricos (demografia, integração comercial, câmbio) não são isolados.
3. **O ciclo 2023 a 2026 está incompleto.** Conclusões sobre ele são preliminares e sensíveis a revisão de dados.
4. **Índices codificados por especialistas** (V-Dem, ITUC, IPS) carregam julgamento humano. São usados como contexto institucional, nunca como evidência isolada.
5. **Séries administrativas** (CadÚnico, MTE, SISDEPEN) refletem capacidade de Estado, não apenas o fenômeno medido. Variações podem decorrer de mudança na coleta.
6. **A desagregação racial** depende de autodeclaração, cuja distribuição mudou ao longo do período.

---

## 11. Protocolo de Reprodutibilidade

Requisitos para publicação:

* Matriz de indicadores, composição dos agregados de controle e definição das janelas temporais **congeladas antes da primeira extração de dados**. Alterações posteriores são registradas com data e justificativa em changelog público.
* Toda série publicada acompanhada de fonte, data de extração e versão da base.
* Código de tratamento e dados brutos disponibilizados junto à publicação.
* Resultados marcados como frágeis nos testes da seção 2.4 identificados visualmente no material final.

---

*Versão 2.0. Documento de especificação metodológica para análise histórica socioeconômica do Brasil, 2002 a 2026.*
