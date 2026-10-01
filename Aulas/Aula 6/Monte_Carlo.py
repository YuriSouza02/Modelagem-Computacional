# -*- coding: utf-8 -*-
"""Modelagem Computacional"""

import time
import matplotlib.pyplot as plt
import numpy as np


def estimar_pi_monte_carlo(n_pontos: int = 1000):
    """Calcula a estimativa de Pi e devolve as coordenadas e a máscara de pontos dentro do círculo."""
    rng = np.random.default_rng()
    x = rng.uniform(0.0, 1.0, n_pontos)
    y = rng.uniform(0.0, 1.0, n_pontos)

    # Condição para o ponto pertencer ao quarto de círculo unitário (x^2 + y^2 <= 1)
    dentro = (x**2 + y**2) <= 1.0
    n_area = np.sum(dentro)

    pi_estimado = 4.0 * (n_area / n_pontos)
    return x, y, dentro, pi_estimado


def main():
    n_pontos = 1000

    tempo_inicio = time.time()
    x, y, dentro, pi_estimado = estimar_pi_monte_carlo(n_pontos)
    tempo_fim = time.time()

    tempo_execucao = tempo_fim - tempo_inicio

    # Exibição dos resultados numéricos
    print(f"Valor estimado de π: {pi_estimado:.5f}")
    print(f"Valor real de π:     {np.pi:.5f}")
    print(f"Erro absoluto:       {abs(pi_estimado - np.pi):.5f}")
    print(f"Tempo de execução:   {tempo_execucao:.6f} segundos")

    # Gráfico de dispersão dos pontos da simulação
    plt.figure(figsize=(6, 6))
    plt.scatter(x[dentro], y[dentro], color='red', s=15, label='Dentro do círculo')
    plt.scatter(x[~dentro], y[~dentro], color='green', s=15, label='Fora do círculo')

    # Desenho do arco do quarto de círculo teórico f(x) = sqrt(1 - x^2)
    x_curva = np.linspace(0, 1, 200)
    plt.plot(x_curva, np.sqrt(1 - x_curva**2), color='blue', linewidth=2, label=r'$f(x) = \sqrt{1 - x^2}$')

    plt.title(f"Estimativa de Monte Carlo para $\pi$ ($N = {n_pontos}$)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis('square')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Histogramas das distribuições das variáveis x e y
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].hist(x, bins=30, color='skyblue', edgecolor='black')
    axes[0].set_title("Distribuição da Variável X")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("Frequência")
    axes[0].grid(True)

    axes[1].hist(y, bins=30, color='salmon', edgecolor='black')
    axes[1].set_title("Distribuição da Variável Y")
    axes[1].set_xlabel("y")
    axes[1].set_ylabel("Frequência")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()