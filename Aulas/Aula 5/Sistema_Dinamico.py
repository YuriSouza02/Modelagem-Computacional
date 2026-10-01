# -*- coding: utf-8 -*-
"""Modelagem Computacional 5"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sympy as sp


def analisar_sistema_simbolico():
    """Realiza a análise simbólica do sistema: pontos fixos, Jacobiana e estabilidade."""
    # Definição explícita de variáveis e parâmetros
    f, r = sp.symbols('f r')
    g_0, g_1 = sp.symbols('g_0 g_1')
    c_0, c_1 = sp.symbols('c_0 c_1')
    d_0, d_1 = sp.symbols('d_0 d_1')

    u = sp.Matrix([f, r])

    # Sistema de equações de transição F(u)
    F = sp.Matrix([
        u[0] + g_0 * u[0] - c_0 * u[0] * u[1] - d_0 * f**2,
        u[1] + g_1 * u[1] - c_1 * u[0] * u[1] - d_1 * r**2
    ])

    # Parâmetros numéricos
    param_valores = {
        g_0: 0.047, c_0: 0.012, d_0: 0.003,
        g_1: 0.023, c_1: 0.015, d_1: 0.0015
    }

    F_num = F.subs(param_valores)
    delta = u - F_num
    J = F_num.jacobian(u)

    print("--- Vetor de Estado u ---")
    sp.pprint(u)

    print("\n--- Sistema Numérico F(u) ---")
    sp.pprint(F_num)

    # Resolução dos pontos fixos
    pontos_fixos = sp.solve(delta, u, dict=True)
    print("\n--- Pontos Fixos e Análise de Estabilidade ---")
    for idx, pt in enumerate(pontos_fixos, start=1):
        print(f"\nPonto Fixo {idx}:")
        for var, val in pt.items():
            print(f"  {var} = {float(val):.5f}")

        # Avaliação da Matriz Jacobiana no ponto fixo
        J_pt = J.subs(pt)
        autovalores = J_pt.eigenvals()

        print("  Autovalores da Jacobiana:")
        for ev, mult in autovalores.items():
            val_comp = complex(ev)
            modulo = abs(val_comp)
            print(f"    λ = {val_comp:.5f} | Módulo |λ| = {modulo:.5f} (mult: {mult})")


def simular_sistema(n_iteracoes: int = 50, f0: float = 25.0, r0: float = 30.0) -> pd.DataFrame:
    """Executa a simulação numérica do modelo para N iterações."""
    # Parâmetros
    g_0, c_0, d_0 = 0.047, 0.012, 0.003
    g_1, c_1, d_1 = 0.023, 0.015, 0.0015

    historico = [{'f': f0, 'r': r0}]

    for _ in range(n_iteracoes):
        f_atual = historico[-1]['f']
        r_atual = historico[-1]['r']

        f_prox = f_atual + g_0 * f_atual - c_0 * f_atual * r_atual - d_0 * (f_atual**2)
        r_prox = r_atual + g_1 * r_atual - c_1 * f_atual * r_atual - d_1 * (r_atual**2)

        historico.append({'f': f_prox, 'r': r_prox})

    return pd.DataFrame(historico)


def main():
    # 1. Análise simbólica e cálculo de estabilidade
    analisar_sistema_simbolico()

    # 2. Simulação numérica
    df_simulacao = simular_sistema(n_iteracoes=50, f0=25.0, r0=30.0)

    print("\n--- Primeiras Iterações da Simulação ---")
    print(df_simulacao.head(10))

    # 3. Visualização dos resultados
    plt.figure(figsize=(10, 4))

    # Série temporal
    plt.subplot(1, 2, 1)
    plt.plot(df_simulacao['f'], 'r-o', label='$f_n$', markersize=4)
    plt.plot(df_simulacao['r'], 'b-o', label='$r_n$', markersize=4)
    plt.title("Evolução Temporal das Populações")
    plt.xlabel("Iteração ($n$)")
    plt.ylabel("População")
    plt.legend()
    plt.grid(True)

    # Plano de fase
    plt.subplot(1, 2, 2)
    plt.plot(df_simulacao['f'], df_simulacao['r'], 'g-o', markersize=4)
    plt.title("Plano de Fase ($f_n$ vs $r_n$)")
    plt.xlabel("$f_n$")
    plt.ylabel("$r_n$")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()