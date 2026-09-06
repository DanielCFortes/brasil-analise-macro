# Relatório de Extração e Limitações

**Extração de 06/09/2026 | Base World Bank atualizada em 13/07/2026 | Especificação v3.0**

---

## 1. O que foi extraído

| Item | Resultado |
| :--- | :--- |
| Fonte | World Bank API (WDI e PIP) |
| Indicadores solicitados | 30 |
| Indicadores com dado | 29 |
| Observações | 8.732 |
| Países | Brasil mais 11 comparadores mais o agregado Upper Middle Income |
| Período | 1995 a 2026 (análise em 2002 a 2026, camada 0 em 1995 a 2001) |

Entregues: painel completo, tabela de desempenho diferencial por regime e matriz de cobertura.

### Verificação de sanidade (Brasil)

Os valores conferem com o que se conhece da realidade brasileira, o que indica que a extração está correta.

| Indicador | 2002 | 2014 | 2024 |
| :--- | ---: | ---: | ---: |
| Pobreza extrema US$ 3,00 PPC (%) | 16,2 | 4,8 | 3,0 |
| Índice de Gini | 58,1 | 52,1 | 50,3 |
| PIB per capita PPC (int$ 2021) | 14.266 | 19.183 | 19.652 |
| Mortalidade infantil (por mil) | 25,6 | 14,0 | 12,3 |
| Saneamento básico (% pop.) | 75,1 | 84,9 | 92,4 |
| Desemprego (%) | 10,6 | 6,8 | 6,8 |

---

## 2. Limitações que quebram a especificação v3

Estes quatro pontos exigem decisão sua antes de congelar a metodologia. Não são detalhes de execução.

### 2.1 O buraco de 2020 não existe na base internacional, e isso é um problema

A v3 determina que 2020 não seja interpolado, porque a PNAD Contínua anual não foi a campo. **Mas o World Bank PIP tem valor de pobreza e Gini para o Brasil em 2020.** Ele é derivado de fonte alternativa, não de medição direta comparável aos demais anos.

Consequência: a regra da v3 e a base do Tier 1 estão em conflito direto. Ou você aceita o dado do PIP para 2020 e revoga a regra, declarando a origem, ou você remove o ponto e passa a divergir da fonte que diz usar.

Detalhe adicional: **2010 está ausente** na série brasileira de pobreza e Gini, por ser ano censitário sem PNAD. A v3 não previa esse buraco.

### 2.2 A cobertura de distribuição é assimétrica a ponto de comprometer a mediana

Anos com dado observado de pobreza e Gini no período 2002 a 2024:

| País | Anos observados |
| :--- | ---: |
| Brasil | 22 |
| Indonésia, Equador, Peru | 23 a 24 |
| Argentina, Colômbia, Turquia | 21 a 22 |
| China | 16 |
| México | 13 |
| Chile | 10 |
| África do Sul | 5 |
| Índia | 4 |

Índia tem quatro pontos em 22 anos (2004, 2009, 2011, 2022). África do Sul tem cinco. **A mediana do agregado G20 emergentes para indicadores de distribuição é, na prática, interpolação.**

Isso não invalida a comparação, mas obriga a duas coisas: publicar o número de países efetivamente disponíveis em cada célula (já está na planilha, coluna `n_<grupo>`) e rebaixar o G20 emergentes a grupo secundário para indicadores de distribuição.

### 2.3 As janelas de regime não são respeitadas na prática

A janela nominal do boom de commodities é 2003 a 2011. Para o Brasil, os anos efetivamente usados no cálculo foram **2002 a 2012**, porque a rotina busca o ponto disponível mais próximo dentro de uma tolerância.

Pior: países diferentes usam anos de ponta diferentes dentro da mesma janela. Chile compara 2003 com 2011, Índia compara 2004 com 2011.

A coluna `anos_brasil` na planilha registra isso para o Brasil, mas o mesmo registro precisa existir por país antes de publicar. **Sem isso, a crítica "vocês compararam períodos diferentes" é procedente.**

### 2.4 Interpolação linear em série de pesquisa amostral

Para calcular medianas de grupo ano a ano, séries irregulares foram interpoladas linearmente dentro do intervalo observado. Isso suaviza artificialmente reversões que podem ter ocorrido entre duas pesquisas.

O efeito é maior justamente onde a cobertura é pior. Para Índia, uma reta liga 2011 a 2022. Qualquer movimento real nesse intervalo desapareceu.

---

## 3. Indicadores headline sem dado

| Indicador | Pergunta | Situação |
| :--- | :---: | :--- |
| Taxa de informalidade | 1 | **Sem dado.** O código do World Bank retornou vazio e a API do ILOSTAT não respondeu em duas tentativas. Exige download manual do ILOSTAT ou uso da PNAD Contínua (Tier 2), o que quebra a regra de não mistura na comparação internacional. |
| Crescimento da renda do bottom 40 (prosperidade compartilhada) | 2 | **Inutilizável como série.** O indicador do Banco Mundial é uma janela móvel calculada em poucos anos de referência (2014, 2021, 2023, 2024, 2025), não uma série anual. Precisa ser reconstruído a partir dos quintis, que estão extraídos. |
| Insegurança alimentar (FIES) | 3 | **Só a partir de 2015**, com 9 observações. Sem dado para Índia, Turquia e China. Não cobre os regimes I, II e III. |
| Cobertura de proteção social | 4a | **Esparso demais.** Entre 1 e 16 observações por país. China tem 1. Não sustenta comparação por regime. |
| Dívida do governo central sobre PIB | Transversal | **Ausente** para Chile, Argentina, Equador e China. Exige IMF WEO como fonte substituta. |

---

## 4. Indicadores com cobertura frágil

| Indicador | Problema |
| :--- | :--- |
| Homicídios | Indonésia tem 3 observações, Peru 11. O grupo de exportadores de commodities fica com base fraca. No regime de recuperação, dois grupos ficaram abaixo do mínimo de 3 países e o diferencial saiu vazio. |
| Ensino médio completo | Argentina tem 2 observações, China 2, Índia 6. A comparação internacional de educação é fraca. |
| Agregado Upper Middle Income | Retorna sem código ISO na API e cobre apenas 21 dos 29 indicadores. Precisa tratamento próprio ou substituição. |

---

## 5. Fontes ainda não extraídas

Nada abaixo foi tocado nesta rodada. Todas são exigidas pela v3.

**Tier 1 pendente:** WID.world (participação do 1%, Palma, P90/P10), UNODC direto, V-Dem, ITUC Global Rights Index, World Prison Brief, IMF WEO (fiscal), WHO (excesso de mortalidade para o Benchmark B da pandemia), Penn World Table (produtividade alternativa).

**Tier 2 pendente, integralmente:** IBGE/PNAD Contínua, DataSUS/SIM, INEP, SNIS, CadÚnico, BCB, FBSP, Tesouro, Receita Federal, MTE, SISDEPEN.

**Consequência prática: não existe nenhuma desagregação por raça, região, gênero ou situação do domicílio nos dados atuais.** A seção 6 da v3 está inteiramente por fazer, e ela está no bloco obrigatório.

---

## 6. Disponibilidade do período final

| Grupo de indicadores | Último ano |
| :--- | ---: |
| PIB, produtividade, desemprego, investimento, inflação | 2025 |
| Pobreza, Gini, quintis, mortalidade, saneamento, vacinação | 2024 |
| Homicídios, insegurança alimentar | 2023 |
| Cobertura de proteção social | 2022 |

Confirma empiricamente a limitação 4 da v3: o ciclo 2023 a 2026 tem, na melhor das hipóteses, dois anos de dado social. Qualquer conclusão sobre ele é preliminar.

---

## 7. Resultados preliminares que merecem atenção

Não são conclusões. São achados que vão gerar discussão e que você deve verificar antes de publicar.

**7.1 Correção. Variação em pontos percentuais não é comparável entre níveis iniciais diferentes.** Uma versão anterior deste relatório afirmava que o Brasil superou os demais emergentes no boom de commodities. **A afirmação estava errada e está corrigida aqui.**

Medido em pontos percentuais, no boom o Brasil reduziu pobreza extrema **menos que os três grupos**: 9,8 pontos, contra 11,7 da mediana latino americana, 17,2 do G20 sem China e 14,9 dos exportadores de commodities.

A causa é o ponto de partida. Em 2004 a Índia estava em 46,4%, a Indonésia em 45,4% e a África do Sul em 42,1%, contra 16,2% do Brasil em 2002. Quem parte de um nível três vezes maior cai mais em pontos percentuais sem ter feito nada melhor.

Medido em **redução proporcional**, o quadro muda: Brasil menos 60%, América Latina menos 68%, G20 sem China menos 43%, exportadores menos 43%. O Brasil supera dois dos três grupos e continua atrás apenas da América Latina.

**Consequência para a especificação:** as duas medidas passam a ser obrigatórias e publicadas juntas. Nenhuma sozinha sustenta conclusão.

**7.2 Dois resultados sobrevivem às duas métricas.** Na recessão e ajuste (2015 a 2018) o Brasil é o pior dos quatro nas duas medidas: piora de 2,2 pontos, ou mais 46% em termos relativos, enquanto o G20 sem China melhorou 43%. Na recuperação (2022 em diante) o Brasil é o melhor dos quatro nas duas medidas: menos 4,5 pontos e menos 60%.

Esses dois achados são robustos à escolha da medida. O do boom não é, e por isso não deve ser publicado como conclusão.

**7.3 Produtividade e PIB per capita divergem no regime de recuperação.** PIB per capita cresce, produtividade fica estável ou levemente negativa. É exatamente a distinção que motivou promover produtividade a headline.

**7.4 Na recessão e ajuste, todos os indicadores de distribuição pioram, e pioram mais que nos pares.** É o resultado mais consistente entre grupos até agora.

---

## 8. Decisões necessárias antes de seguir

0. **Métrica de variação:** adotar pontos percentuais e redução proporcional sempre juntos, e revisar todos os resultados já calculados sob a segunda medida
1. **2020:** aceitar o valor do PIP declarando a origem, ou remover o ponto e divergir da fonte
2. **Interpolação:** manter com declaração explícita, ou restringir as comparações apenas a anos com dado observado nos dois lados
3. **Janelas:** fixar tolerância zero (só compara quem tem dado nos anos exatos) ou registrar por país os anos usados
4. **Informalidade:** download manual do ILOSTAT, ou aceitar PNAD Contínua com quebra da regra de não mistura
5. **G20 emergentes em distribuição:** rebaixar a secundário ou manter com aviso de cobertura

Resolvidas essas cinco, o próximo passo é a extração do Tier 2, que é onde está a desagregação e o volume real de trabalho.
