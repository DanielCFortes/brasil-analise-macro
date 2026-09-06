# Metodologia de Análise Socioeconômica e de Direitos: Brasil (2002 a 2026)

**Versão 3.0 | Documento público de especificação metodológica**

Este documento define o framework metodológico, conceitual e operacional para analisar a evolução do crescimento econômico, do bem estar, da desigualdade e das garantias de direitos no Brasil entre 2002 e 2026, com comparação internacional explícita.

Por ser destinado a publicação, o documento declara antecipadamente o desenho analítico, os testes de robustez obrigatórios, os limites do que a análise pode concluir e as objeções previsíveis com suas respostas. A especificação é congelada antes da coleta de dados.

---

## Changelog em relação à versão 2.0

| Mudança | Motivo |
| :--- | :--- |
| "Contrafactual" substituído por **desempenho diferencial** | Diferença de deltas é comparação descritiva, não contrafactual causal |
| Crescimento econômico promovido a **eixo central** | PIB, PIB per capita e produtividade estavam rebaixados a contexto |
| Adicionada **camada de trajetória anterior a 2002** | Evita atribuir ao período tendências que já estavam em curso |
| Mandatos rebaixados de unidade analítica a **camada narrativa** | Elimina a tensão com a ausência declarada de atribuição causal |
| Commodities promovido de teste de robustez a **eixo estrutural** | É o mecanismo central do período 2003 a 2011 |
| Adicionada métrica de **crescimento inclusivo** | Conecta crescimento, distribuição e bem estar numa estrutura só |
| Sensibilidade de lag movida de mandatos para **eventos discretos** | Calibrar lag sobre mandato contradiz o rebaixamento acima |
| Adicionado **Benchmark B de pandemia com critérios numéricos congelados** | Evita seleção de grupo de comparação após ver os dados |
| Mobilidade social reduzida a **corte pontual** | Não existe painel intergeracional anual para 24 anos no Brasil |
| Adicionadas seções de **objeções antecipadas** e **corte de escopo** | Requisitos de publicação e de viabilidade de execução |

---

## 1. Objetivo e Escopo

**Pergunta central:** como mudou a vida dos brasileiros entre 2002 e 2026, quem se beneficiou do crescimento, quanto do movimento foi compartilhado com países comparáveis, onde o Brasil se diferenciou e qual foi o custo econômico e fiscal dessa trajetória.

A análise se organiza em cinco perguntas independentes mais uma transversal. **Cada uma pode ter resposta diferente. Não há tentativa de unificá-las em narrativa única.**

| # | Pergunta | Eixo |
| :---: | :--- | :--- |
| 1 | O Brasil ficou mais rico? | Crescimento e produtividade |
| 2 | Quem capturou o crescimento? | Distribuição |
| 3 | A vida da população pobre melhorou? | Bem estar material absoluto |
| 4a | O cidadão ficou mais protegido? | Proteção social e direitos do trabalho |
| 4b | O cidadão ficou mais seguro e com mais direitos civis? | Segurança e Estado de direito |
| 5 | O Brasil fez isso melhor ou pior que países comparáveis? | Desempenho diferencial |
| T | A que custo? | Camada fiscal transversal |

As perguntas 4a e 4b são separadas deliberadamente. Cobertura previdenciária e taxa de homicídios não são manifestações do mesmo fenômeno e não devem ser agregadas no mesmo índice ou na mesma leitura.

**Período de análise:** 2002 a 2026. O ciclo 2023 a 2026 está incompleto e é reportado como parcial.

**Período de referência histórica:** 1995 a 2001, usado apenas como benchmark interno. Séries anteriores a 1994 não são utilizadas para renda, pobreza ou desigualdade, por inviabilidade decorrente da hiperinflação.

**Recorte populacional:** população total para as perguntas 1 e 2; foco nos 40% de menor rendimento para as perguntas 3, 4a e 4b. Desagregação obrigatória conforme seção 6.

---

## 2. Desenho Analítico

### 2.1 Desempenho diferencial

A métrica principal de comparação internacional é:

> **Desempenho diferencial = (variação do Brasil no período) menos (variação da mediana do grupo de comparação no mesmo período)**

Se a pobreza extrema cai 8 pontos no Brasil e 7 pontos na mediana dos emergentes, o desempenho diferencial é de 1 ponto. Ambos os números são publicados lado a lado, sempre.

**O que essa métrica não é.** Ela não é um contrafactual. Não permite afirmar que 1 ponto da melhora foi causado por fatores domésticos. O diferencial pode refletir composição demográfica, exposição a commodities, severidade do choque, estrutura produtiva, câmbio ou tendência prévia. O termo contrafactual é reservado a análises que construam explicitamente a trajetória esperada do Brasil na ausência de um choque, o que está fora do escopo desta especificação.

### 2.2 Posição percentílica

Métrica secundária: o **percentil do Brasil dentro do grupo de comparação** em cada ano. É imune à composição do grupo e responde de forma direta se o Brasil melhorou ou apenas acompanhou a melhora geral.

### 2.3 Quatro camadas de comparação

**Camada 0. Trajetória histórica interna (1995 a 2001).** Antes de qualquer comparação internacional, verifica se a evolução observada após 2002 representa continuidade, aceleração, desaceleração ou reversão de tendência anterior.

Aplicada obrigatoriamente a: mortalidade infantil, escolarização, saneamento, homicídios, renda, desigualdade e emprego. **Não é identificação causal. É benchmark interno.**

Sem essa camada, tendências de longo prazo já em curso desde os anos 90 seriam lidas como excepcionalidade do período analisado.

**Camada A. Série anual contínua.** Unidade básica de análise. Todos os gráficos são anuais, com eventos marcados como linhas verticais.

**Camada B. Regimes econômicos.** Unidade principal de agrupamento. Definida por condições externas, não por calendário político.

| Regime | Anos |
| :--- | :--- |
| Boom de commodities | 2003 a 2011 |
| Desaceleração pós boom | 2012 a 2014 |
| Recessão e ajuste | 2015 a 2018 |
| Pandemia | 2020 a 2021 |
| Recuperação | 2022 a 2026 |

Esta é a única partição temporal usada para cálculo de deltas. Nenhum outro esquema de períodos aparece na análise.

**Camada C. Mandatos presidenciais. Camada narrativa apenas.** Os mandatos são sobrepostos visualmente à série anual para contextualização. **Não são unidade de cálculo de delta, não recebem atribuição de resultado e não são ranqueados.**

Formulação correta: "2003 a 2011, expansão associada ao boom de commodities", com os governos correspondentes indicados na visualização. Formulação incorreta: "o governo X reduziu a pobreza em N pontos".

### 2.4 Commodities como eixo estrutural

O ciclo de commodities não é ruído a ser removido. É o mecanismo central de interpretação do período 2003 a 2011 e é analisado explicitamente na cadeia:

> preços de commodities → termos de troca → exportações → atividade econômica → emprego → arrecadação → capacidade de transferência → renda das famílias

Cada elo é medido com indicador próprio. O benchmark de exportadores líquidos (seção 4) verifica quanto do desempenho brasileiro foi compartilhado com países expostos ao mesmo choque externo.

### 2.5 Pandemia: dois benchmarks

O choque da COVID-19 foi global, mas a magnitude da resposta fiscal foi escolha doméstica. Para separar efeito do choque de diferença na resposta:

**Benchmark A.** Brasil contra todos os grupos de comparação.

**Benchmark B.** Brasil contra o subconjunto de países com choque e capacidade fiscal comparáveis.

**Critérios do Benchmark B, congelados antes da extração e definidos apenas por números:**

* Excesso de mortalidade acumulado em 2020 e 2021 por 100 mil habitantes dentro de mais ou menos 40% do valor brasileiro (fonte: estimativas da OMS)
* Dívida bruta sobre PIB em 2019 dentro de mais ou menos 20 pontos percentuais do valor brasileiro (fonte: IMF WEO)

A composição resultante é publicada antes da análise dos resultados. **Nenhum país entra ou sai do Benchmark B após a visualização dos dados.** Sem esses critérios numéricos, um grupo de comparação escolhido por "similaridade" após ver os resultados é seleção post hoc e invalidaria a comparação.

### 2.6 Sensibilidade de lag em eventos discretos

Políticas têm tempos de transmissão diferentes. Transferência de renda é rápida, saneamento e educação são lentos.

A análise de sensibilidade de lag (0, 1, 2 e 3 anos) é aplicada **exclusivamente a eventos discretos com data conhecida**, e não a mandatos:

* Unificação e expansão do Bolsa Família (2003 e 2004)
* Regra de valorização do salário mínimo (2007)
* Reforma Trabalhista (2017)
* Emenda do Teto de Gastos (2016)
* Reforma da Previdência (2019)
* Auxílio Emergencial (2020)
* Recomposição do Bolsa Família e novo arcabouço fiscal (2023)

Se uma associação só aparece em um lag específico, isso é reportado como fragilidade, não escondido.

### 2.7 Testes de robustez obrigatórios

**Teste 1. Termos de troca.** Resultados do período 2003 a 2011 recalculados contra o subgrupo de exportadores líquidos de commodities. Se a vantagem brasileira desaparecer nessa comparação, a conclusão do período é revista.

**Teste 2. Composição do grupo.** Cada resultado recalculado com e sem China no agregado G20 emergentes, e com exclusão sequencial de cada país do agregado latino americano. Resultados que invertem sinal com a saída de um único país são marcados como frágeis.

**Teste 3. Recorte temporal.** Deslocamento das janelas de regime em mais ou menos 1 ano. Achados que só existem em um recorte específico não são publicados como conclusão.

**Teste 4. Fonte.** Onde houver série nacional e série internacional para o mesmo fenômeno, ambas são plotadas. Divergência de direção entre elas é reportada.

---

## 3. Arquitetura de Dados

### 3.1 Dois tiers, sem mistura

**Tier 1. Comparação internacional.** Exclusivamente bases já harmonizadas entre países. Nenhuma fonte nacional entra neste tier, **inclusive para o Brasil**.

| Domínio | Base |
| :--- | :--- |
| Pobreza, Gini, renda do bottom 40, prosperidade compartilhada | World Bank PIP |
| PIB, PIB per capita, PPC, investimento | World Bank WDI |
| Produtividade do trabalho | ILOSTAT / Penn World Table |
| Emprego, informalidade, subutilização, previdência | ILOSTAT |
| Desenvolvimento humano e IDH-D | UNDP |
| Saneamento | JMP (WHO / UNICEF) |
| Educação | UNESCO UIS |
| Homicídios | UNODC |
| Insegurança alimentar | FAO SOFI (escala FIES) |
| Concentração no topo, Palma, P90/P10 | WID.world |
| Mortalidade infantil | UN IGME |
| Cobertura vacinal | WHO WUENIC |
| Excesso de mortalidade na pandemia | WHO |
| Fiscal | IMF WEO |
| Direitos do trabalho | ITUC Global Rights Index |
| Institucional | V-Dem |
| Encarceramento | World Prison Brief |

**Tier 2. Brasil em alta resolução.** IBGE, DataSUS, INEP, SNIS, CadÚnico, BCB, FBSP, Tesouro, Receita Federal, MTE, SISDEPEN. É neste tier que ocorre toda a desagregação.

### 3.2 Regra de não mistura

O valor do Brasil em qualquer gráfico comparativo vem do Tier 1, mesmo quando difere do valor oficial do IBGE. As séries divergem por definição metodológica. A divergência é documentada uma vez, em nota técnica, e não é reconciliada.

### 3.3 Estrutura de apresentação

1. Brasil absoluto, com Tier 1 e Tier 2 lado a lado
2. Brasil desagregado, apenas Tier 2
3. Brasil relativo aos grupos de comparação, apenas Tier 1

Brasil absoluto e Brasil relativo nunca aparecem no mesmo gráfico sem rótulo explícito de qual é qual.

---

## 4. Grupos de Comparação

Calculados por **mediana**, não média, para evitar dominância de outliers. Composição congelada antes da primeira extração e não alterada após a visualização dos resultados.

| Grupo | Composição | Uso |
| :--- | :--- | :--- |
| América Latina | México, Colômbia, Chile, Peru, Argentina, Equador | Principal |
| G20 emergentes | Índia, Indonésia, África do Sul, Turquia, México, China | Principal, sempre reportado com e sem China |
| Emergentes amplo | Agregado "upper middle income" do Banco Mundial | Principal |
| Exportadores líquidos de commodities | Chile, Colômbia, Peru, África do Sul, Indonésia | Teste 1 |
| Benchmark de pandemia | Definido por critérios numéricos da seção 2.5 | Período 2020 a 2021 |

**Ajustes monetários.** Comparações de renda e pobreza em US$ PPC de 2021. A linha internacional de pobreza extrema vigente é **US$ 3,00 por dia em PPC de 2021**, revisada pelo Banco Mundial em junho de 2025, com as linhas complementares em US$ 4,20 e US$ 8,30. A série histórica é baixada já recalculada do World Bank PIP. Nenhuma conversão manual é realizada.

---

## 5. Matriz de Indicadores

### Pergunta 1. O Brasil ficou mais rico?

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| PIB real per capita em PPC | Headline | IBGE | World Bank WDI |
| Produtividade do trabalho | Headline | IBGE / IPEA | ILOSTAT |
| Taxa de informalidade | Headline | PNAD Contínua | ILOSTAT |
| Investimento sobre PIB | Suporte | IBGE | World Bank WDI |
| Desemprego e subutilização | Suporte | PNAD Contínua | ILOSTAT |
| Salário real médio | Suporte | PNAD Contínua | ILOSTAT |

Produtividade é o indicador que distingue ganho de renda sustentável de ganho de renda financiado por termos de troca ou por expansão de crédito. É obrigatório.

### Pergunta 2. Quem capturou o crescimento?

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Crescimento da renda do bottom 40 versus renda média | Headline | PNAD Contínua | World Bank PIP (prosperidade compartilhada) |
| Índice de Gini | Headline | PNAD Contínua | World Bank PIP |
| Participação do 1% mais rico | Headline | DIRPF / Receita | WID.world |
| Palma ratio | Suporte | PNAD Contínua | WID.world |
| P90/P10 | Suporte | PNAD Contínua | WID.world |
| Salário mínimo real | Suporte | MTE / IPEA | sem equivalente |
| Percentual da força de trabalho no piso | Suporte | PNAD Contínua | sem equivalente |

O salário mínimo é lido junto ao percentual da força de trabalho que recebe o piso e à indexação de aposentadorias e BPC, que são os canais efetivos de transmissão.

### Pergunta 3. A vida da população pobre melhorou?

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Renda real do bottom 40 | Headline | PNAD Contínua | World Bank PIP |
| Taxa de extrema pobreza | Headline | IBGE | World Bank PIP |
| Insegurança alimentar | Headline | PENSSAN / POF | FAO SOFI (FIES) |
| Mortalidade infantil | Headline | DataSUS | UN IGME |
| Acesso a saneamento | Suporte | PNAD Contínua, calibrada por Censo | JMP |
| Conclusão do ensino médio (18 a 24 anos) | Suporte | INEP / IBGE | UNESCO UIS |
| Cobertura vacinal | Suporte | PNI / DataSUS | WHO WUENIC |
| Acesso ao ensino superior por quintil de renda e raça | Suporte | PNAD Contínua | sem equivalente |

O último indicador é a versão viável da dimensão de mobilidade social. Ver seção 11, limitação 7.

### Pergunta 4a. O cidadão ficou mais protegido?

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Cobertura previdenciária | Headline | INSS / PNAD | ILOSTAT |
| Cobertura de transferência de renda | Headline | MDS | ILO Social Protection |
| Índice de direitos sindicais e trabalhistas | Suporte | não aplicável | ITUC Global Rights Index |
| Fiscalização trabalhista | Suporte | MTE | sem equivalente |
| Resgates de trabalho análogo à escravidão | Suporte | MTE | sem equivalente |

### Pergunta 4b. O cidadão ficou mais seguro e com mais direitos civis?

| Indicador | Nível | Fonte BR | Fonte internacional |
| :--- | :--- | :--- | :--- |
| Taxa de homicídios | Headline | SIM / DataSUS | UNODC |
| Mortes por causa indeterminada | Headline, obrigatório | SIM / DataSUS | não aplicável |
| Mortes por intervenção policial | Suporte | FBSP | não aplicável |
| Taxa de encarceramento | Suporte | SISDEPEN | World Prison Brief |
| Índice de democracia igualitária | Suporte | não aplicável | V-Dem |

**Protocolo de homicídios.** A série principal do Brasil é SIM/DataSUS (mortes por agressão), por ser registro de saúde e menos sujeito a incentivo de classificação policial. A série de mortes por causa indeterminada é publicada **sempre no mesmo gráfico**, porque em alguns estados absorve homicídios reclassificados. Sem ela, uma queda pode ser reclassificação. Comparações internacionais usam exclusivamente UNODC.

### Pergunta transversal. A que custo?

| Indicador | Fonte BR | Fonte internacional |
| :--- | :--- | :--- |
| Dívida bruta sobre PIB | Tesouro / BCB | IMF WEO |
| Resultado primário | Tesouro | IMF WEO |
| Gasto social sobre PIB | Tesouro / SIOP | IMF / ILO |
| Inflação da base (INPC) | IBGE | não comparável |
| Comprometimento de renda com dívida das famílias | BCB / PEIC | sem equivalente |

Não é pilar. Roda por baixo das cinco perguntas e responde se o ganho de bem estar do período foi financiado ou antecipado do período seguinte.

---

## 6. Desagregação Obrigatória

Média nacional oculta trajetórias divergentes. Numa análise sobre desigualdade brasileira, a desagregação não é detalhe metodológico, é frequentemente o próprio achado.

Todo indicador headline do Tier 2 é publicado desagregado por:

* **Região:** cinco macrorregiões, com destaque Nordeste versus Sudeste
* **Raça e cor:** classificação IBGE
* **Gênero**
* **Situação do domicílio:** urbano e rural

Indicadores de suporte são desagregados quando a fonte permitir. Ausência de desagregação é declarada explicitamente, nunca omitida.

---

## 7. Quebras Metodológicas e Lacunas

| Situação | Tratamento |
| :--- | :--- |
| PNAD antiga (até 2011) e PNAD Contínua (a partir de 2012) | Séries reportadas separadamente, com marcador de quebra. Sem encadeamento retroativo. |
| 2020, suspensão da coleta presencial da PNAD Contínua anual | Não interpolar. PNAD COVID usada apenas para direção, nunca para nível. Comparações ancoradas em 2019 e 2021. |
| Censo 2010 e 2022, sem Censo 2020 | Suplemento anual da PNAD Contínua como série contínua; Censos usados apenas para calibração de nível. |
| CadÚnico | Não é proxy de pobreza. É indicador próprio de cobertura e focalização. Aumento pode indicar mais pobreza ou mais busca ativa, e a análise não separa os dois efeitos. |
| Linha internacional de pobreza | US$ 3,00 em PPC de 2021. Série baixada já recalculada do PIP. |
| Inflação da base | INPC (cesta de 1 a 5 salários mínimos) para custo de vida real dos estratos inferiores. IPCA usado apenas quando exigido por comparabilidade internacional. |
| Série anterior a 1994 | Não utilizada para renda, pobreza ou desigualdade. |
| Autodeclaração racial | A distribuição mudou ao longo do período. Séries desagregadas por raça trazem nota. |

**Regra visual:** nenhum gráfico exibe linha contínua atravessando quebra metodológica.

---

## 8. Cronologia de Referência

Eventos verificáveis, sem interpretação. A caracterização de cada período é escrita **após** a análise dos dados.

| Período | Mandato | Eventos verificáveis |
| :---: | :---: | :--- |
| 2003 a 2006 | Lula I | Unificação do Bolsa Família; alta do índice de preços de commodities |
| 2007 a 2010 | Lula II | Regra de valorização do salário mínimo; crise financeira global de 2008; PAC; expansão do crédito consignado |
| 2011 a 2014 | Dilma I | Transição para a PNAD Contínua; queda do índice de preços de commodities a partir de 2011 |
| 2015 a 2018 | Dilma II e Temer | Recessão de 2015 e 2016; impeachment; Emenda do Teto de Gastos; Reforma Trabalhista |
| 2019 a 2022 | Bolsonaro | Reforma da Previdência; pandemia de COVID-19; Auxílio Emergencial; Novo Marco do Saneamento; choque inflacionário global |
| 2023 a 2026 | Lula III | Recomposição do Bolsa Família; novo arcabouço fiscal; Reforma Tributária do consumo. Período parcial. |

---

## 9. Validação Macro

Aplicados ao final da série, para verificar coerência com os indicadores anuais:

1. **IDH-D:** perda de desenvolvimento humano provocada pela desigualdade
2. **IPS:** qualidade de vida sem neutralização pelo PIB
3. **Índice de Gini:** trajetória da distribuição de renda domiciliar

Os três também são reportados em formato de desempenho diferencial.

**Nota sobre o Gini.** Pesquisas domiciliares subestimam sistematicamente a renda do topo. O Gini é sempre publicado ao lado da participação do 1% mais rico apurada por dados tributários. Gini em queda com concentração no topo estável é resultado possível e não é apresentado como contradição.

---

## 10. Princípio Interpretativo

A análise não busca uma narrativa única para 24 anos. Resultados possíveis e legítimos incluem:

* O Brasil melhorou muito, mas acompanhou tendência global
* O Brasil melhorou muito e superou seus pares
* O crescimento foi baixo, mas a distribuição dos ganhos foi progressiva
* O crescimento foi forte, mas os ganhos foram concentrados
* A melhora social foi expressiva, acompanhada de deterioração institucional
* O resultado depende fortemente do período, do indicador e do benchmark

**Chegar a conclusões diferentes em dimensões diferentes não é falha da análise. É a característica mais importante a preservar.**

---

## 11. Limitações Declaradas

Declaradas antes da coleta, não após.

1. **A análise não estabelece causalidade entre política específica e resultado.** Mede evolução, distribuição e desempenho relativo. Atribuição de crédito ou culpa a governos individuais está fora do escopo.
2. **Desempenho diferencial não é contrafactual.** Ver seção 2.1.
3. **A hipótese de tendências comparáveis pode falhar.** É testada para commodities, composição do grupo e severidade da pandemia. Outros canais assimétricos, como demografia, integração comercial e regime cambial, não são isolados.
4. **O período 2023 a 2026 está incompleto.** Conclusões são preliminares e sensíveis a revisão de dados.
5. **Índices codificados por especialistas** (V-Dem, ITUC, IPS) carregam julgamento humano. São usados como contexto institucional, nunca como evidência isolada.
6. **Séries administrativas** (CadÚnico, MTE, SISDEPEN) refletem capacidade de Estado, não apenas o fenômeno medido.
7. **Mobilidade intergeracional não é medida como série.** O Brasil não possui painel longitudinal intergeracional cobrindo o período. A dimensão é aproximada por acesso ao ensino superior por quintil de renda e raça, que é medida de oportunidade, não de mobilidade realizada.
8. **A camada anterior a 2002 tem menor qualidade de dado.** A PNAD antiga não foi a campo em anos censitários e a comparabilidade com a PNAD Contínua é limitada.

---

## 12. Objeções Antecipadas

Objeções previsíveis à publicação, com a resposta metodológica e a seção onde está o tratamento. **Esta seção é publicada junto com a análise.**

### Sobre recorte temporal

| Objeção | Resposta | Seção |
| :--- | :--- | :--- |
| "Vocês escolheram o recorte que favorece o governo X" | Partição temporal única, definida por condições econômicas externas, congelada antes da extração. Teste 3 desloca as janelas em mais ou menos 1 ano e reporta o efeito. | 2.3, 2.7 |
| "Por que começa em 2002 e não em 1994?" | 2002 é o início da série de análise. A camada 0 inclui 1995 a 2001 justamente para verificar se a tendência já existia. Séries de renda anteriores a 1994 são inviáveis pela hiperinflação. | 2.3, 7 |
| "2026 ainda não acabou" | Correto. O período é declarado parcial e não recebe conclusão fechada. | 1, 11.4 |
| "O período escolhido corta a Reforma X ao meio" | Eventos discretos recebem análise própria de lag 0 a 3, independente da partição por regime. | 2.6 |

### Sobre grupo de comparação

| Objeção | Resposta | Seção |
| :--- | :--- | :--- |
| "Vocês compararam o Brasil com países muito diferentes" | Três agregados independentes com composições distintas, mais posição percentílica, que é imune a composição. | 2.2, 4 |
| "Se tirar a China o resultado muda" | Todo resultado do G20 emergentes é publicado com e sem China por padrão. | 2.7, 4 |
| "O grupo foi montado para dar esse resultado" | Composição congelada antes da primeira extração. Alterações posteriores ficam registradas em changelog público com data e justificativa. Teste 2 exclui cada país sequencialmente. | 2.7, 13 |
| "O Benchmark B da pandemia foi escolhido a dedo" | Critérios exclusivamente numéricos (excesso de mortalidade e dívida sobre PIB em 2019), definidos e publicados antes de ver os resultados. | 2.5 |
| "Por que não comparar com países ricos?" | O objetivo é desempenho relativo a países de renda e estrutura comparáveis. Comparação com economias avançadas mede distância de desenvolvimento, que é outra pergunta. | 4 |

### Sobre dados e fontes

| Objeção | Resposta | Seção |
| :--- | :--- | :--- |
| "Esse número não bate com o do IBGE" | Comparações internacionais usam exclusivamente bases harmonizadas, inclusive para o Brasil. A divergência é esperada e documentada. Séries nacionais aparecem separadamente. | 3.2, 3.3 |
| "A linha de pobreza mudou, os números antigos estavam errados?" | O Banco Mundial revisou a linha em 2025 e recalculou a série histórica. Usamos a série recalculada de ponta a ponta. Comparação com publicações anteriores exige atenção à linha usada. | 4, 7 |
| "A queda de homicídios é real ou é reclassificação?" | Mortes por causa indeterminada são publicadas no mesmo gráfico, obrigatoriamente, justamente para permitir essa avaliação. | 5, Pergunta 4b |
| "A pobreza caiu ou só aumentou o cadastro?" | CadÚnico não é usado como medida de pobreza. É indicador separado de cobertura. | 7 |
| "A informalidade mudou de definição no meio da série" | Quebra PNAD antiga e PNAD Contínua marcada visualmente, sem encadeamento retroativo. | 7 |
| "Por que INPC e não IPCA?" | INPC reflete a cesta de consumo de famílias de 1 a 5 salários mínimos, que é a população analisada. IPCA aparece quando exigido por comparabilidade internacional. | 7 |
| "E o buraco de 2020?" | Declarado. A PNAD Contínua anual não foi a campo. Não interpolamos. Comparações do período usam 2019 e 2021 como âncoras. | 7 |

### Sobre interpretação política

| Objeção | Resposta | Seção |
| :--- | :--- | :--- |
| "Isso é um ranking de presidentes disfarçado" | Mandatos são camada narrativa sobreposta à série, sem cálculo de delta e sem atribuição de resultado. A unidade de agrupamento é o regime econômico. | 2.3 |
| "Foi tudo commodities" | Hipótese tratada como eixo estrutural, não como ressalva. A cadeia de transmissão é medida e o Teste 1 compara o Brasil com outros exportadores líquidos. | 2.4, 2.7 |
| "Foi tudo programa social" | As perguntas 1, 2 e 3 são separadas exatamente para permitir que crescimento, distribuição e bem estar tenham respostas diferentes. | 1 |
| "Vocês ignoram o custo fiscal" | Camada transversal obrigatória, presente em toda leitura de período. | 5 |
| "Os índices de democracia são ideológicos" | V-Dem e ITUC são codificados por especialistas e essa limitação está declarada. Entram como contexto institucional de suporte, nunca como evidência isolada nem como headline. | 11.5 |
| "A conclusão já estava escrita antes" | Especificação congelada e publicada antes da extração; changelog com data e justificativa para qualquer alteração; código e dados brutos publicados. | 13 |
| "Vocês vão concluir o que quiserem porque tem indicador demais" | Indicadores headline definidos antes da coleta. Resultados frágeis nos testes de robustez são marcados visualmente no material final. | 2.7, 13 |

### Sobre o que a análise não faz

| Objeção | Resposta |
| :--- | :--- |
| "Isso não prova causalidade, então não serve para nada" | Correto quanto à causalidade. A análise responde o que aconteceu, quem capturou o ganho, quanto foi compartilhado com países comparáveis e a que custo fiscal. Essas quatro perguntas têm resposta empírica e raramente são respondidas juntas no debate público. |
| "Falta a dimensão Y" | Escopo declarado na seção 14, com o que ficou de fora e por quê. |

---

## 13. Protocolo de Reprodutibilidade

* Matriz de indicadores, composição dos grupos de comparação, definição das janelas de regime e critérios do Benchmark B **congelados e publicados antes da primeira extração de dados**
* Qualquer alteração posterior registrada em changelog público com data e justificativa
* Toda série publicada acompanhada de fonte, data de extração e versão da base
* Código de tratamento e dados brutos disponibilizados junto à publicação
* Resultados marcados como frágeis nos testes da seção 2.7 identificados visualmente no material final
* Financiamento e vínculos institucionais do autor declarados na publicação

---

## 14. Escopo: Obrigatório e Opcional

O escopo desta especificação é grande para execução individual. A divisão abaixo define o que precisa existir para publicar e o que entra apenas se houver capacidade.

### Obrigatório para publicar

* Todos os indicadores headline das cinco perguntas e da camada fiscal
* Camada 0 (anterior a 2002) para os sete indicadores listados em 2.3
* Três grupos de comparação principais, com desempenho diferencial e percentil
* Testes 1, 2 e 3
* Desagregação por região e raça dos headline do Tier 2
* Seções 11, 12 e 13 publicadas junto com a análise

### Opcional, se houver capacidade

* Indicadores de suporte (Palma, P90/P10, investimento, cobertura vacinal, encarceramento, fiscalização trabalhista)
* Benchmark B de pandemia
* Sensibilidade de lag completa nos sete eventos discretos
* Desagregação por gênero e por situação do domicílio
* Teste 4 (comparação de fontes)
* Acesso ao ensino superior por quintil e raça

### Fora de escopo, declarado

* Atribuição causal a políticas ou governos
* Controle sintético ou qualquer contrafactual construído
* Mobilidade intergeracional como série temporal
* Análise subnacional por estado ou município
* Projeções para além de 2026

---

*Versão 3.0. Documento de especificação metodológica para análise histórica socioeconômica do Brasil, 2002 a 2026. Congelar antes da primeira extração de dados.*
