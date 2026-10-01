# -*- coding: utf-8 -*-
"""Modelagem Computacional"""

import matplotlib.pyplot as plt
import numpy as np

# Configurações globais de estilo do Matplotlib
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "figure.dpi": 200
})


def simular_crescimento_logistico(p0: float, h: int, k_val: float, p_lim_val: float) -> np.ndarray:
    """Calcula a evolução populacional utilizando a discretização do modelo logístico."""
    p = np.zeros(h)
    p[0] = p0
    for i in range(1, h):
        p[i] = p[i - 1] + k_val * p[i - 1] * (p_lim_val - p[i - 1])
    return p


def main():
    # Parâmetros do modelo
    h = 19         # Quantidade de horas
    p0 = 9.6       # População inicial
    p_lim_n = 10   # Quantidade de valores de população limite
    k_n = 4        # Quantidade de valores de k

    # Dados experimentais
    dados_exatos = np.array([
        9.6, 18.3, 29.0, 47.2, 71.1, 119.1, 174.6, 350.7, 441.0,
        513.3, 559.7, 594.8, 629.4, 640.8, 651.1, 655.9, 659.6, 661.8, 661.8
    ])

    # Vetores de suporte e parâmetros
    n = np.arange(h)
    k_valores = 0.00084 + 0.00002 * np.arange(k_n)
    p_lim_valores = np.arange(660, 660 + p_lim_n)

    # Simulação e geração dos gráficos
    for p_lim in p_lim_valores:
        plt.figure()
        plt.plot(n, dados_exatos, 'o-r', label='Dados Exatos')

        for k in k_valores:
            p = simular_crescimento_logistico(p0, h, k, p_lim)
            plt.plot(n, p, 'o-', label=f'k = {k:.5f}')

        plt.title(f"População Limite ($p_{{lim}}$) = {p_lim}")
        plt.xlabel("Tempo (horas)")
        plt.ylabel("População")
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.grid(True)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()