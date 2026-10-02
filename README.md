# Compilado de Modelagem Computacional (Aulas 1 a 12)

Este repositório reúne os projetos, simulações numéricas, análises de estabilidade e ambientes de Aprendizado por Reforço desenvolvidos ao longo das aulas de **Modelagem Computacional**. A estrutura dos arquivos segue a organização dos diretórios exibida no projeto:

---

## 📌 Sumário Geral

1. [Aula 1: Simulação de Crescimento Populacional Logístico](https://www.google.com/search?q=%23aula-1-simula%C3%A7%C3%A3o-de-crescimento-populacional-log%C3%ADstico)
2. [Aula 2: Modelo Logístico em Diferenças Finitas](https://www.google.com/search?q=%23aula-2-modelo-log%C3%ADstico-em-diferen%C3%A7as-finitas)
3. [Aula 3: Análise de Estabilidade de Sistemas Dinâmicos Discretos (2D)](https://www.google.com/search?q=%23aula-3-an%C3%A1lise-de-estabilidade-de-sistemas-din%C3%A2micos-discretos-2d)
4. [Aula 4: Análise de Estabilidade de Sistemas Dinâmicos Discretos (3D)](https://www.google.com/search?q=%23aula-4-an%C3%A1lise-de-estabilidade-de-sistemas-din%C3%A2micos-discretos-3d)
5. [Aula 5: Modelagem Dinâmica com Competição Intraespecífica](https://www.google.com/search?q=%23aula-5-modelagem-din%C3%A2mica-com-competi%C3%A7%C3%A3o-intraespec%C3%ADfica)
6. [Aula 6: Estimação de pi via Método de Monte Carlo e LCG](https://www.google.com/search?q=%23aula-6-estima%C3%A7%C3%A3o-de-%5Cpi-via-m%C3%A9todo-de-monte-carlo-e-lcg)
7. [Aula 7: Simulação Estocástica de Controle de Estoque](https://www.google.com/search?q=%23aula-7-simula%C3%A7%C3%A3o-estoc%C3%A1stica-de-controle-de-estoque)
8. [Aula 8: Simulação de Eventos Discretos — Gestão de Estoque de Pneus](https://www.google.com/search?q=%23aula-8-simula%C3%A7%C3%A3o-de-eventos-discretos--gest%C3%A3o-de-estoque-de-pneus)
9. [Aula 9: Análise Comparativa de Desempenho Escolar (Teste t vs. Permutação)](https://www.google.com/search?q=%23aula-9-an%C3%A1lise-comparativa-de-desempenho-escolar-teste-t-vs-permuta%C3%A7%C3%A3o)
10. [Aula 10: Aprendizado por Reforço com CartPole-v0](https://www.google.com/search?q=%23aula-10-aprendizado-por-refor%C3%A7o-com-cartpole-v0)
11. [Aula 11: Controle Contínuo em MountainCarContinuous-v0](https://www.google.com/search?q=%23aula-11-controle-cont%C3%ADnuo-em-mountaincarcontinuous-v0)
12. [Aula 12: Ambiente Personalizado Gymnasium — ShowerEnv](https://www.google.com/search?q=%23aula-12-ambiente-personalizado-gymnasium--showerenv)

---

## Aula 1: Simulação de Crescimento Populacional Logístico

Este projeto realiza a modelagem computacional e simulação numérica do crescimento populacional logístico ao longo de 19 horas, comparando os resultados teóricos com dados experimentais reais.

### 📐 Modelo Matemático

A simulação utiliza o método numérico discreto para aproximar a equação logística:

$$P_i = P_{i-1} + k \cdot P_{i-1} \cdot (P_{\text{lim}} - P_{i-1})$$

Onde:

* $P_i$: População na hora $i$
* $k$: Taxa de crescimento populacional ($0{,}00084$ a $0{,}00090$)
* $P_{\text{lim}}$: Capacidade limite / capacidade de carga ($660$ a $669$)
* $P_0$: População inicial ($9{,}6$)

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **NumPy** — Manipulação de vetores e matrizes
* **Matplotlib** — Visualização e geração de gráficos comparativos

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python "Aulas/Aula 1/Crescimento_Populacional.py"

```

### 📊 Resultados

O script gera 10 gráficos comparando a curva dos dados reais com 4 curvas simuladas para diferentes coeficientes de $k$ sob variadas populações limite ($P_{\text{lim}}$).

---

## Aula 2: Modelo Logístico em Diferenças Finitas

Este projeto formaliza a simulação do crescimento populacional de um organismo ao longo do tempo utilizando o **Modelo Logístico** em diferenças finitas:

$$P_{n+1} = P_n + k \cdot P_n \cdot (P_{\text{lim}} - P_n)$$

O objetivo é comparar dados empíricos observados ao longo de 19 horas com simulações numéricas, variando a taxa de crescimento ($k$) e a capacidade de carga ($P_{\text{lim}}$).

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **NumPy**: Manipulação de vetores e cálculos numéricos.
* **Matplotlib**: Visualização gráfica das curvas do modelo em comparação com os dados reais.

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python "Aulas/Aula 2/Decaimento_concentracao.py"

```

### 📊 Estrutura do Código

* **Dados de Entrada**: Série temporal com 19 pontos de medição da população.
* **Variação de Parâmetros**:
* $k$: Testa valores de $0{,}00084$ a $0{,}00090$.
* $P_{\text{lim}}$: Testa limites populacionais entre $660$ e $669$.


* **Saída**: Gráficos comparando os dados exatos com as curvas estimadas para cada combinação de parâmetros.

---

## Aula 3: Análise de Estabilidade de Sistemas Dinâmicos Discretos (2D)

Análise de estabilidade de um sistema dinâmico discreto linear de duas variáveis de estado ($R$ e $J$) utilizando computação simbólica via **SymPy**.

### 📐 Modelo Matemático

O sistema é representado na forma matricial por $u_{k+1} = F(u_k)$, onde o vetor de estados é:

$$u = \begin{bmatrix} R \\ J \end{bmatrix}$$

A função de transição $F(R, J)$ é dada por:

$$F(R, J) = \begin{bmatrix} a_R R + p_R J \\ p_J R + a_J J \end{bmatrix}$$

Aplicando os parâmetros ($a_R = 0{,}5$, $a_J = 0{,}7$, $p_R = 0{,}2$ e $p_J = 0{,}5$):

$$F(R, J) = \begin{bmatrix} 0{,}5 R + 0{,}2 J \\ 0{,}5 R + 0{,}7 J \end{bmatrix}$$

### 🔬 Etapas da Análise

1. **Pontos Fixos ($u^*$):** Resolução do sistema $u - F(u) = 0$ para determinação dos pontos de equilíbrio.
2. **Matriz Jacobiana ($J_M$):** Cálculo da matriz de derivadas parciais:

$$J_M = \begin{bmatrix} \frac{\partial F_1}{\partial R} & \frac{\partial F_1}{\partial J} \\ \frac{\partial F_2}{\partial R} & \frac{\partial F_2}{\partial J} \end{bmatrix}$$

3. **Autovalores ($\lambda$):** Obtenção dos autovalores da matriz Jacobiana.
4. **Critério de Estabilidade Discreta:**
* Se $\vert{}\lambda\vert{} < 1$ para todos os autovalores, o ponto fixo é **Estável**.
* Se pelo menos um autovalor satisfazer $\vert{}\lambda\vert{} > 1$, o ponto fixo é **Instável**.



### 🚀 Como Executar

```bash
pip install sympy
python "Aulas/Aula 3/Analise_Sensibilidade_Linear.py"

```

---

## Aula 4: Análise de Estabilidade de Sistemas Dinâmicos Discretos (3D)

Análise simbólica e numérica de equilíbrio e estabilidade de um sistema dinâmico discreto não linear com três variáveis de estado ($O$, $H$ e $M$).

### 📐 Modelo Matemático

O sistema é representado por $u_{k+1} = F(u_k)$, onde o vetor de estados é:

$$u = \begin{bmatrix} O \\ H \\ M \end{bmatrix}$$

A função de transição não linear $F(O, H, M)$ é dada por:

$$F(O, H, M) = \begin{bmatrix} (1+k_1) O - k_4 O H + k_9 O M \\ (1+k_2) H - k_5 O H + k_8 H M \\ (1+k_3) M - k_6 O M - k_7 H M \end{bmatrix}$$

#### Parâmetros do Modelo

* $k_1 = 0{,}01$, $k_2 = 0{,}01$, $k_3 = 100$
* $k_4 = 0{,}001$, $k_5 = 0{,}001$, $k_6 = 0{,}005$
* $k_7 = 0{,}05$, $k_8 = 0{,}001$, $k_9 = 0{,}001$

### 🔬 Etapas da Análise

1. **Pontos Fixos ($u^*$):** Resolução do sistema não linear $u - F(u) = 0$.
2. **Matriz Jacobiana ($J_M$):** Cálculo simbólico da matriz de ordem $3 \times 3$:

$$J_M = \begin{bmatrix}  \frac{\partial F_1}{\partial O} & \frac{\partial F_1}{\partial H} & \frac{\partial F_1}{\partial M} \\ \frac{\partial F_2}{\partial O} & \frac{\partial F_2}{\partial H} & \frac{\partial F_2}{\partial M} \\ \frac{\partial F_3}{\partial O} & \frac{\partial F_3}{\partial H} & \frac{\partial F_3}{\partial M}  \end{bmatrix}$$

3. **Avaliação Numérica:** Substituição dos parâmetros numéricos $k_1 \dots k_9$ nas soluções de equilíbrio e na matriz Jacobiana.
4. **Critério de Estabilidade Discreta:** Avaliação do módulo dos autovalores ($\vert{}\lambda\vert{} < 1 \implies$ Estável, $\vert{}\lambda\vert{} > 1 \implies$ Instável).

### 🚀 Como Executar

```bash
pip install sympy
python "Aulas/Aula 4/Analise_Sensibiliade_nao_linear.py"

```

---

## Aula 5: Modelagem Dinâmica com Competição Intraespecífica

Simulação e análise de um sistema dinâmico discreto de duas populações interativas ($f$ e $r$) com termos quadráticos representando a **competição intraespecífica** por recursos ambientais limitados.

### 📐 Modelo Matemático

$$\begin{cases}  f_{n+1} = (1 + g_0) f_n - c_0 f_n r_n - d_0 f_n^2 \\  r_{n+1} = (1 + g_1) r_n - c_1 f_n r_n - d_1 r_n^2  \end{cases}$$

Onde:

* $f_n, r_n$: Variáveis de estado representando as populações no instante $n$.
* $g_0, g_1$: Taxas intrínsecas de crescimento populacional.
* $c_0, c_1$: Coeficientes de interação interespecífica.
* $d_0, d_1$: Coeficientes de competição intraespecífica (fator de limitação da capacidade de carga).

### 🔬 Etapas do Algoritmo

1. **Modelagem Simbólica (SymPy)**: Definição formal do vetor de estados $u = [f, r]^T$ e do sistema $F(f, r)$.
2. **Atribuição de Parâmetros e Condições Iniciais**:
* Condição Inicial: $f_0 = 25$, $r_0 = 30$
* Parâmetros: $g_0 = 0{,}047$, $c_0 = 0{,}012$, $d_0 = 0{,}003$ | $g_1 = 0{,}023$, $c_1 = 0{,}015$, $d_1 = 0{,}0015$


3. **Simulação Numérica**: Resolução iterativa ao longo de $50$ passos de tempo.
4. **Estruturação Tabular (Pandas)**: Organização dos dados simulados em um `DataFrame`.
5. **Visualização Gráfica (Matplotlib)**: Plotagem da evolução temporal e do **Plano de Fase** ($f_n \text{ vs. } r_n$).

### 🚀 Como Executar

```bash
pip install sympy pandas matplotlib
python "Aulas/Aula 5/Sistema_Dinamico.py"

```

---

## Aula 6: Estimação de $\pi$ via Método de Monte Carlo e LCG

Aplicação da **Simulação de Monte Carlo** para estimar a constante $\pi$, utilizando um **Gerador Congruencial Linear (LCG)** para amostragem pseudorrandômica.

### 📐 Modelo Matemático

#### 1. Relação de Áreas e Monte Carlo

Para um quadrado unitário de área $A_{\text{quadrado}} = 1$ e um quarto de círculo inscrito de raio $r = 1$ ($A_{\text{círculo}} = \frac{\pi}{4}$), a curva limite é $f(x) = \sqrt{1 - x^2}, x \in [0, 1]$.

Sortear $N$ pontos aleatórios no quadrado permite estimar $\pi$ por:

$$\frac{N_{\text{área}}}{N} \approx \frac{A_{\text{círculo}}}{A_{\text{quadrado}}} = \frac{\pi}{4} \implies \pi \approx 4 \cdot \frac{N_{\text{área}}}{N}$$

#### 2. Gerador Congruencial Linear (LCG)

$$X_{n+1} = (a \cdot X_n + b) \pmod c$$

Com parâmetros: $a = 7^5 = 16807$, $b = 0$, $c = 62$.

### 🔬 Etapas do Algoritmo

1. **Geração de Dados:** Vetores de tamanho $N = 1000$ para coordenadas $x$ e $y$ em $[0, 1]$.
2. **Classificação Geométrica:** Avaliação da condição $y_i < f(x_i)$ (dentro do círculo: vermelho; fora: verde).
3. **Métricas:** Medição do tempo de execução e cálculo da estimativa de $\pi$.
4. **Análise de Frequência:** Plotagem de histogramas de distribuição.

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python "Aulas/Aula 6/Monte_Carlo.py"

```

---

## Aula 7: Simulação Estocástica de Controle de Estoque

Simulação estocástica da gestão de estoque e otimização do lote de reposição ($T$) ao longo de 100 meses via **LCG** e **Método da Transformação Inversa**.

### 📐 Modelo Matemático e Regras de Negócio

#### 1. Gerador Congruencial Linear (LCG)

$$X_{n+1} = (a \cdot X_n + b) \pmod c \quad (a = 16807, b = 0, c = 61)$$

#### 2. Distribuição da Demanda Mensal ($Y$)

Variável aleatória discreta $Y \in \{1, 2, 3, 4\}$:

$$P(Y = y) = \begin{cases}  0{,}1, & \text{se } y = 1 \\  0{,}2, & \text{se } y = 2 \\  0{,}6, & \text{se } y = 3 \\  0{,}1, & \text{se } y = 4  \end{cases}$$

#### 3. Dinâmica Financeira e de Estoque

A cada mês ($R = 100$):

* **Receita:** $+20 \times \min(\text{Estoque}, Y)$
* **Armazenamento:** $-5 \times \text{Estoque restante}$
* **Reposição:** Se $\text{Estoque} < 30$, repõe $+T$ unidades ao custo de $-10 \times T$.

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python "Aulas/Aula 7/simulacao_estocastica.py"

```

---

## Aula 8: Simulação de Eventos Discretos — Gestão de Estoque de Pneus

Simulação de eventos discretos e Monte Carlo em Python para modelar o comportamento do nível de estoque e a lucratividade acumulada de uma revenda de pneus ao longo de 52 semanas.

### 📐 Modelo Matemático

#### 1. Gerador Congruencial Linear (LCG)

$$X_{n+1} = (a \cdot X_n) \pmod c \quad (a = 16807, c = 2^{31} - 1)$$

#### 2. Inversão da Distribuição Acumulada

* **Atraso na Entrega ($A$):** $P(A=1)=0{,}30$, $P(A=2)=0{,}40$, $P(A=3)=0{,}30$.
* **Demanda Diária ($D$):** Valores em $\{25, 30, 35, 40, 45, 50, 55\}$ com probabilidades acumuladas associadas.

### ⚙️ Regras de Negócio e Parâmetros

* **Preço de Venda:** $100 / unidade
* **Custo de Falta (Penalidade):** $80 / unidade não atendida
* **Custo de Estocagem:** $5 / unidade restante por dia
* **Lote de Reposição (Recarga):** 240 unidades por ciclo
* **Duração da Simulação:** 52 semanas

### 🚀 Como Executar

```bash
pip install matplotlib
python "Aulas/Aula 8/Simulacao_Financeira.py"

```

---

## Aula 9: Análise Comparativa de Desempenho Escolar (Teste t vs. Permutação)

Análise estatística inferencial comparando o desempenho médio em exames entre estudantes de dois municípios (**Goiânia** e **Vitória**), utilizando o **Teste t de Student** e um **Teste de Permutação não-paramétrico** (Monte Carlo).

### 📐 Metodologia Estatística

| Método | Tipo | Suposições |
| --- | --- | --- |
| **Teste t de Student** | Paramétrico | Exige normalidade da distribuição subjacente das notas. |
| **Teste de Permutação** | Não-paramétrico | Livre de distribuição; constrói a distribuição nula empírica via 10.000 reamostragens sem reposição. |

### 🚀 Como Executar

```bash
pip install numpy matplotlib scipy
python "Aulas/Aula 9/Analise_estatistica.py"

```

---

## Aula 10: Aprendizado por Reforço com CartPole-v0

Introdução aos ambientes de Aprendizado por Reforço da biblioteca **OpenAI Gym / Gymnasium**, focada no problema de equilíbrio da barra sobre o carrinho (**CartPole-v0**).

### 📌 Especificações do Ambiente

* **Objetivo:** Manter o mastro equilibrado na vertical aplicando forças horizontais.
* **Espaço de Ações:** Discreto (`0`: Empurra para esquerda, `1`: Empurra para direita).
* **Espaço de Observações (4D):**

| Índice | Variável | Mínimo | Máximo |
| --- | --- | --- | --- |
| **0** | Posição do carrinho | -4.8 | 4.8 |
| **1** | Velocidade do carrinho | $-\infty$ | $\infty$ |
| **2** | Ângulo do mastro | -0.418 rad (-24°) | 0.418 rad (24°) |
| **3** | Velocidade angular | $-\infty$ | $\infty$ |

### 🚀 Como Executar

```bash
pip install gymnasium numpy opencv-python moviepy
python "Aulas/Aula 10/OpenIA_Gym.py"

```

---

## Aula 11: Controle Contínuo em MountainCarContinuous-v0

Configuração e avaliação de políticas em um ambiente de controle contínuo, onde um veículo precisa acumular energia potencial para subir uma colina.

### 📌 Especificações do Ambiente

* **Espaço de Ações:** Contínuo em $[-1.0, 1.0]$ (força para a esquerda ou direita).
* **Espaço de Observações (2D):**

| Índice | Variável | Mínimo | Máximo |
| --- | --- | --- | --- |
| **0** | Posição do carrinho | -1.2 | 0.6 |
| **1** | Velocidade do carrinho | -0.07 | 0.07 |

### 🚀 Como Executar

```bash
pip install gymnasium box2d-py pyvirtualdisplay numpy opencv-python moviepy
python "Aulas/Aula 11/OpenIA_MountainCarContinuous.py"

```

---

## Aula 12: Ambiente Personalizado Gymnasium — ShowerEnv

Desenvolvimento e simulação de um ambiente personalizado compatível com **Gymnasium** para controle automático de temperatura de água em um misturador térmico de chuveiro.

### 📌 Especificações do Ambiente `ShowerEnv`

* **Ações:** `Box(low=0.0, high=1.0, shape=(2,))` $\rightarrow$ $[F_{\text{quente}}, F_{\text{frio}}]$
* **Observações:** `Box(low=0.0, high=100.0, shape=(1,))` $\rightarrow$ $[T_{\text{mix}}]$
* **Condição Inicial:** $T_0 = 20^\circ\text{C}$ | **Meta:** $T_{\text{alvo}} = 38^\circ\text{C}$ | **Limite:** 30 passos.

### 🧮 Modelagem Matemática

#### 1. Mistura Térmica

$$T_{\text{mix}} = \frac{F_{\text{quente}} \cdot T_{\text{quente}} + F_{\text{frio}} \cdot T_{\text{frio}}}{F_{\text{quente}} + F_{\text{frio}}}$$

*(Caso $F_{\text{quente}} + F_{\text{frio}} = 0$, mantém-se a temperatura do passo anterior).*

#### 2. Ruído Estocástico

$$\text{Ruído} \sim U(0.0, 0.1)$$

#### 3. Função de Recompensa

$$r = -\left( \vert{}T_{\text{mix}} - T_{\text{alvo}}\vert{} + 0.1 \cdot (F_{\text{frio}} + F_{\text{quente}}) + F_{\text{quente}} \right)$$

### 🛠️ Requisitos e Execução

```bash
pip install gymnasium numpy matplotlib
python "Aulas/Aula 12/Reinforcement_Learning.py"

```
