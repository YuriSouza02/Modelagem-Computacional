# -*- coding: utf-8 -*-
"""Modelagem Computacional"""

import matplotlib.pyplot as plt
import numpy as np


def gerar_procura(rng: np.random.Generator, n_amostras: int) -> np.ndarray:
    """Gera amostras da variável aleatória discreta de procura de stock."""
    valores = np.array([1, 2, 3, 4])
    probabilidades = np.array([0.1, 0.2, 0.6, 0.1])
    return rng.choice(valores, size=n_amostras, p=probabilidades)


def simular_controle_estoque(
    rng: np.random.Generator,
    meses: int = 100,
    m_ponto_pedido: int = 30,
    t_quantidade_pedido: int = 5,
    estoque_inicial: int = 200
) -> tuple[float, int]:
    """Simula a gestão de stock ao longo de um determinado período de meses."""
    estoque = estoque_inicial
    lucro_total = 0.0

    procuras = gerar_procura(rng, meses)

    for procura in procuras:
        # Vendas realizadas no mês corrente
        vendas = min(estoque, procura)
        lucro_total += 20 * vendas

        # Atualização do stock remanescente e custo de manutenção
        estoque -= vendas
        lucro_total -= 5 * estoque

        # Reposição de stock caso atinja o ponto de pedido M
        if estoque < m_ponto_pedido:
            estoque += t_quantidade_pedido
            lucro_total -= 10 * t_quantidade_pedido

    lucro_medio = lucro_total / meses
    return lucro_medio, estoque


def main():
    # Inicialização do gerador de números pseudoaleatórios
    rng = np.random.default_rng(seed=42)

    # 1. Histograma da Variável Aleatória de Procura
    amostras_va = gerar_procura(rng, 1000)

    plt.figure(figsize=(7, 4))
    plt.hist(
        amostras_va,
        bins=np.arange(0.5, 5.5, 1),
        rwidth=0.8,
        color='skyblue',
        edgecolor='black'
    )
    plt.title("Distribuição de Frequência da Procura (V.A.)")
    plt.xlabel("Procura (unidades)")
    plt.ylabel("Frequência")
    plt.xticks([1, 2, 3, 4])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # 2. Simulação de sensibilidade para a quantidade de encomenda T (1 a 9)
    meses = 100
    m_ponto_pedido = 30

    t_valores = list(range(1, 10))
    lucros_medios = []
    estoques_finais = []

    for t in t_valores:
        lucro_m, est_final = simular_controle_estoque(
            rng,
            meses=meses,
            m_ponto_pedido=m_ponto_pedido,
            t_quantidade_pedido=t
        )
        lucros_medios.append(lucro_m)
        estoques_finais.append(est_final)
        print(f"M: {m_ponto_pedido} | T: {t} | Lucro Médio: {lucro_m:.2f} | Stock Final: {est_final}")

    # 3. Gráfico dos resultados da simulação
    plt.figure(figsize=(8, 5))
    plt.plot(t_valores, lucros_medios, 'r-o', label='Lucro Médio por Mês')
    plt.plot(t_valores, estoques_finais, 'b-s', label='Stock Final')

    plt.title("Simulação do Controlo de Stock em Função de $T$")
    plt.xlabel("Quantidade de Reposição ($T$)")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()