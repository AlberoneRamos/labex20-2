# Uma Análise Comparativa de Repositórios Python

## Introdução

No desenvolvimento de software, simplicidade e expressividade são características importantes na escolha de uma linguagem de programação. No contexto em que sistemas precisam ser desenvolvidos de forma ágil, linguagens de simples prototipação e com uma baixa curva de aprendizado ganham cada vez mais espaço no mercado. Entretanto, a balança entre agilidade e qualidade é uma questão relevante neste cenário, uma vez que os desenvolvedores tendem a priorizar entregas rápidas e releases constantes em detrimento de padrões de qualidade mais alto. Dessa forma, o objetivo deste laboratório é analisar a qualidade de repositórios desenvolvidos na linguagem Python, comparando-os sob a perspectiva de características levantadas por uma _baseline_ definida a seguir.

## Metodologia

### 1. Elaboração do Baseline

Atualmente, a linguagem Python possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Entretanto, ela foi inicialmente proposta por [Guido van Rossum](https://github.com/gvanrossum), cuja participaço ainda é ativa na manutenção da linguagem.

Dessa forma, iniciaremos nosso laboratório através da definição de uma _baseline_ de comparação para as métricas analisadas. Para tanto, coletaremos cada uma das métricas definidas na Seção 4 para todos os repositórios Python (que não sejam _fork_) do criador da linguagem. Utilizaremos os valores obtidos como base de comparação para as métricas coletadas dos repositórios Python mais populares do GitHub. 

### 2. Seleção de Repositórios Python

Com o objetivo de analisar repositórios relevantes, escritos na linguagem estudada, coletaremos os top-1000 repositórios Python mais populares do GitHub, calculando cada uma das métricas definidas na Seção 4.

### 3. Definição de Questões de Pesquisa

Desta forma, este laboratório tem o objetivo de responder às seguintes questões de pesquisa:

**RQ 01:** Quais as características dos repositórios Python do Guido van Rossum?

**RQ 02:** Quais as características dos top-1000 repositórios Python mais populares?

**RQ 03:** Repositórios populares Python são de boa qualidade?    

**RQ 04:** A popularidade influencia nas características de repositórios Python?

### 4. Definição de Métricas

Utilizaremos como fatores de qualidade métricas associadas à quatro dimensões, tais como: 

* **Popularidade:** número de estrelas, número de watchers, número de forks

* **Tamanho:** linhas de código (LOC)

* **Atividade:** número de releases, frequência de releases (número de releases / dias)

* **Maturidade:** idade (em anos)

### 5. Coleta e Análise de Métricas

Para análise das métricas de popularidade, atividade e maturidade, serão coletadas informações dos repositórios de ambos os conjuntos (_baseline_ e _top-1000_) utilizando as APIs REST ou GraphQL do GitHub. Para medição dos valores de tamanho, utilizaremos uma ferramenta de análise estática de código (por exemplo, o [radon](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)). 

As questões de pesquisa 1 e 2 serão respondidas a partir da análise quantitativa de cada uma métricas (recomenda-se a utilização de valores medianos). Para a RQ 03, os valores obtidos nas RQs 01 e 02 devem ser comparados e discutidos individualmente. Por fim, na RQ 04, os resultados apresentados na RQ 02 devem ser separados em dois grupos (_top_, com os 250 mais populares do dataset; e _bottom_, com os 250 menos populares). Em seguida, a diferença da mediana dos valores de cada uma das métricas deve ser discutidas para ambos os grupos.

## Relatório Final

Para cada uma questões de pesquisa anteriores, faça uma sumarização dos dados obtidos através de [valores medianos](https://www.sciencebuddies.org/science-fair-projects/science-fair/summarizing-your-data#meanmedianandmode). Mesmo que de forma informal, elabore hipóteses sobre o que você espera de resposta e tente analisar a partir dos valores obtidos.

Elabore um documento que apresente (i) uma introdução simples com hipóteses informais; (ii) a metodologia que você utilizou para responder às questões de pesquisa; (iii) os resultados obtidos para cada uma delas; (iii) a discussão sobre o que você esperava como resultado (suas hipóteses) e os valores obtidos.  

## Processo de Desenvolvimento

Utilize as tags em negrito (**LabXXSYY**) para identificar as entregas deste laboratório. 

### Sprints

**Lab02S01**: criação da baseline (.csv com os valores de todas as métricas dos repositórios do Guido, bem como os scripts de coleta utilizados para mineração e análise dos repositórios) | **Prazo:** 26/03 | **Valor:** 5 pontos

**Lab02S02**: mineração dos repositórios populares Python (.csv com os valores de todas as métricas dos top-1000 repositórios mais populares, bem como os scripts de coleta utilizados para mineração e análise dos repositórios) **Prazo:** 02/04 | **Valor:** 7 pontos

**Lab02S03**: análise dos dados e elaboração do relatório final | **Prazo:** 09/04 | **Valor:** 8 pontos

### Prazos e Avaliação

Este laboratório deve ser desenvolvido em dupla. Para tanto, responda [esta issue](https://github.com/xavierlaerte/labex-20.1/issues/7), apontando a dupla com quem irá trabalhar e o repositório que será utilizado nas Sprints.

**Prazo final:** 09/04 | **Valor total:** 20 pontos | **Desconto de 0.5 pontos por dia de atraso**
