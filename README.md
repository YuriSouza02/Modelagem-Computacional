# Compilado de Modelagem Computacional (Aulas 1 a 12)

---

## Aula 1: Simulação de Crescimento Populacional Logístico

Este projeto realiza a modelagem computacional e simulação numérica do crescimento populacional logístico ao longo de 19 horas, comparando os resultados teóricos com dados experimentais reais.

### 📌 Modelo Matemático

A simulação utiliza o método numérico discreto para aproximar a equação logística:

$$P_i = P_{i-1} + k \cdot P_{i-1} \cdot (P_{\text{lim}} - P_{i-1})$$

Onde:

* $P_i$: População na hora $i$
* $k$: Taxa de crescimento populacional ($0{,}00084$ a $0{,}00090$)
* $P_{\text{lim}}$: Capacidade limite / capacidade de carga ($660$ a $669$)
* $P_0$: População inicial ($9{,}6$)

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **NumPy** — Manipulação e criação de vetores
* **Matplotlib** — Geração e visualização dos gráficos de comparação

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python Crescimento_Populacional.py

```

### 📊 Resultados

O script gera 10 gráficos comparando a curva exata dos dados reais com 4 curvas simuladas para diferentes coeficientes de $k$ sob variadas populações limite ($P_{\text{lim}}$).

---

## Aula 2: Modelo Logístico em Diferenças Finitas

Este projeto formaliza a simulação do crescimento populacional de um organismo ao longo do tempo utilizando o **Modelo Logístico** em diferenças finitas:

$$P_{n+1} = P_n + k \cdot P_n \cdot (P_{\text{lim}} - P_n)$$

O objetivo é comparar dados empíricos observados ao longo de 19 horas com simulações numéricas, variando a taxa de crescimento ($k$) e a capacidade de carga ($P_{\text{lim}}$).

### 🛠️ Tecnologias Utilizadas

* **Python 3**
* **NumPy**: Manipulação de vetores e cálculos numéricos.
* **Matplotlib**: Visualização e plotagem gráfica das curvas do modelo em comparação com os dados reais.

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python Decaimento_de_Concentracao.py

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

Com os parâmetros $a_R = 0{,}5$, $a_J = 0{,}7$, $p_R = 0{,}2$ e $p_J = 0{,}5$:

$$F(R, J) = \begin{bmatrix} 0{,}5 R + 0{,}2 J \\ 0{,}5 R + 0{,}7 J \end{bmatrix}$$

### 🔬 Etapas da Análise

1. **Pontos Fixos ($u^*$):** Resolução do sistema $u - F(u) = 0$ para determinação dos pontos de equilíbrio.
2. **Matriz Jacobiana ($J_M$):** Cálculo da matriz de derivadas parciais:

$$J_M = \begin{bmatrix} \frac{\partial F_1}{\partial R} & \frac{\partial F_1}{\partial J} \\ \frac{\partial F_2}{\partial R} & \frac{\partial F_2}{\partial J} \end{bmatrix}$$

3. **Autovalores ($\lambda$):** Obtenção dos autovalores da matriz Jacobiana.
4. **Critério de Estabilidade Discreta:**
* Se $\vert{}\lambda\vert{} < 1$ para todos os autovalores, o ponto fixo é **Estável**.
* Se pelo menos um autovalor satisfizer $\vert{}\lambda\vert{} > 1$, o ponto fixo é **Instável**.



### 🚀 Como Executar

```bash
pip install sympy
python modelagem_computacional_3.py

```

---

## Aula 4: Análise de Estabilidade de Sistemas Dinâmicos Discretos (3D)

Análise simbólica e numérica de equilíbrio e estabilidade de um sistema dinâmico discreto não linear com três variáveis de estado ($O$, $H$ e $M$).

### 📐 Modelo Matemático

O sistema é representado por $u_{k+1} = F(u_k)$, onde o vetor de estados é:

$$u = \begin{bmatrix} O \\ H \\ M \end{bmatrix}$$

A função de transição não linear $F(O, H, M)$ é expressa por:

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
python modelagem_computacional_4.py

```

---

## Aula 5: Modelagem Dinâmica com Competição Intraespecífica

Simulação e análise de um sistema dinâmico discreto de duas populações interativas ($f$ e $r$) com termos quadráticos representando a **competição intraespecífica** por recursos ambientais limitados.

### 📐 Modelo Matemático

$$\begin{cases} f_{n+1} = (1 + g_0) f_n - c_0 f_n r_n - d_0 f_n^2 \\ r_{n+1} = (1 + g_1) r_n - c_1 f_n r_n - d_1 r_n^2 \end{cases}$$

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
python modelagem_computacional_5.py

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
python modelagem_computacional_1_3.py

```

---

## Aula 7: Simulação Estocástica de Controle de Estoque

Simulação estocástica da gestão de estoque e otimização do lote de reposição ($T$) ao longo de 100 meses via **LCG** e **Método da Transformação Inversa**.

### 📐 Modelo Matemático e Regras de Negócio

#### 1. Gerador Congruencial Linear (LCG)

$$X_{n+1} = (a \cdot X_n + b) \pmod c \quad (a = 16807, b = 0, c = 61)$$

#### 2. Distribuição da Demanda Mensal ($Y$)

Variable aleatória discreta $Y \in \{1, 2, 3, 4\}$:

$$P(Y = y) = \begin{cases}  0{,}1, & \text{se } y = 1 \\  0{,}2, & \text{se } y = 2 \\  0{,}6, & \text{se } y = 3 \\  0{,}1, & \text{se } y = 4  \end{cases}$$

#### 3. Dinâmica Financeira e de Estoque

A cada mês ($R = 100$):

* **Receita:** $+20 \times \min(\text{Estoque}, Y)$
* **Armazenamento:** $-5 \times \text{Estoque restante}$
* **Reposição:** Se $\text{Estoque} < 30$, repõe $+T$ unidades ao custo de $-10 \times T$.

### 🚀 Como Executar

```bash
pip install numpy matplotlib
python modelagem_computacional_7.py

```

---

## Aula 8: Simulação de Eventos Discretos — Gestão de Estoque de Pneus

Simulação de eventos discretos (Monte Carlo) para a gestão de estoque de um lote de pneus ao longo de 52 semanas, modelando incertezas nos tempos de entrega e demanda diária.

### 💻 Código-Fonte

```python
import time
import matplotlib.pyplot as plt

def lcg_random(quantidade, seed=None):
    c = 2**31 - 1    # 2147483647
    if seed is None:
        seed = int(time.time() * 1000) % c
    a = 7**5         # 16807
    
    numeros = []
    estado = seed
    for _ in range(quantidade):
        estado = (a * estado) % c
        numeros.append(estado / c)
    return numeros

def AtrasoSemanal(x):
    if x <= 0.3:
        return 1
    elif x <= 0.7:
        return 2
    else:
        return 3

def DemandaDiaria(x):
    if x <= 0.05:
        return 25
    elif x <= 0.15:
        return 30
    elif x <= 0.35:
        return 35
    elif x <= 0.65:
        return 40
    elif x <= 0.85:
        return 45
    elif x <= 0.95:
        return 50
    else:
        return 55

semanas = 52
custoPneu = 100        
custoFalta = 80        
custoEstoque = 5       
recarga = 240          
estoque = 0
lucro = 0
atrasoPassado = 0

aleatorios = lcg_random(semanas * 10, seed=12345)
rnd_idx = 0

Lucro_list, DemandaSemanal_list, DemandaDia_list, Estoque_list = [], [], [], []

for i in range(semanas):
    atrasoAtual = AtrasoSemanal(aleatorios[rnd_idx])
    rnd_idx += 1
    
    diasSemEntrega = 6 + atrasoAtual - atrasoPassado
    estoque += recarga
    
    for _ in range(diasSemEntrega):
        demanda = DemandaDiaria(aleatorios[rnd_idx])
        rnd_idx += 1
        
        if estoque < demanda:
            lucro += estoque * custoPneu
            lucro -= (demanda - estoque) * custoFalta
            estoque = 0
        else:
            lucro += demanda * custoPneu
            estoque -= demanda
            lucro -= estoque * custoEstoque
            
        Lucro_list.append(lucro)
        Estoque_list.append(estoque)
        DemandaDia_list.append(demanda)
        
    DemandaSemanal_list.append(sum(DemandaDia_list))
    DemandaDia_list = []
    atrasoPassado = atrasoAtual

media_demanda = sum(DemandaSemanal_list) / len(DemandaSemanal_list)
print(f"Demanda semanal média: {media_demanda:.2f}")
print(f"Total dias simulados: {len(Lucro_list)}")

```

### 🔬 Análise e Recomendações

1. **Truncamento de Semente no LCG:** Aplicar o módulo $c = 2^{31}-1$ na semente gerada via timestamp previne *overflow* antes do primeiro ciclo do gerador.
2. **Custo de Aquisição:** Para apurar o lucro líquido real, deve-se abater o custo unitário de compra ($c_{\text{compra}}$) a cada recebimento do lote de recarga (`lucro -= recarga * custoAquisicao`).
3. **Dimensionamento Aleatório:** A reserva de $520$ números aleatórios garante cobertura completa para a duração máxima de ciclos ($52 \times 10$ chamadas no pior caso).

---

## Aula 9: Análise Comparativa de Desempenho Escolar (Teste t vs. Permutação)

Análise estatística inferencial comparando o desempenho médio em exames entre estudantes de dois municípios (**Goiânia** e **Vitória**), utilizando o **Teste t de Student** e um **Teste de Permutação não-paramétrico** (Monte Carlo).

### 📐 Metodologia Estatística

| Método | Tipo | Suposições |
| --- | --- | --- |
| **Teste t de Student** | Paramétrico | Exige normalidade da distribuição subjacente das notas. |
| **Teste de Permutação** | Não-paramétrico | Livre de distribuição; constrói a distribuição nula empírica via 10.000 reamostragens sem reposição. |

### 🛠️ Código e Pipeline de Execução

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Processamento de dados e filtragem por presenca == 1
# Execução do Teste-t e Simulação Monte Carlo (10.000 permutações)

```

### 🚀 Como Executar

```bash
pip install numpy matplotlib scipy
python modelagem_computacional_9.py

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

### 🛠️ Requisitos e Configuração *Headless*

```bash
pip install gymnasium numpy opencv-python moviepy
apt-get install python-opengl xvfb -y

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

### 🛠️ Configuração de Ambientes sem Display (*Headless*)

```bash
pip install gymnasium box2d-py pyvirtualdisplay numpy opencv-python moviepy
apt-get install python-opengl xvfb -y

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
python modelagem_computacional_12.py

```