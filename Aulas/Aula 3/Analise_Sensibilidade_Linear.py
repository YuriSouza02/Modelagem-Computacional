# -*- coding: utf-8 -*-
"""Modelagem Computacional"""

import sympy as sp


def analisar_sistema_dinamico():
    # 1. Definição explícita de variáveis simbólicas
    R, J = sp.symbols('R J')

    # Parâmetros numéricos do sistema
    a_R, a_J = 0.5, 0.7
    p_R, p_J = 0.2, 0.5

    # Vetor de estado u e função de transição F(u)
    u = sp.Matrix([R, J])
    F = sp.Matrix([
        [a_R * u[0] + p_R * u[1]],
        [a_J * u[1] + p_J * u[0]]
    ])

    print("--- Vetor de Estado u ---")
    sp.pprint(u)

    print("\n--- Sistema F(u) ---")
    sp.pprint(F)

    # 2. Resolução dos pontos fixos (u - F = 0)
    pontos_fixos = sp.solve(u - F, u, dict=True)
    print("\n--- Pontos Fixos (u*) ---")
    print(pontos_fixos)

    # 3. Cálculo da Matriz Jacobiana
    matriz_jacobiana = F.jacobian(u)
    print("\n--- Matriz Jacobiana ---")
    sp.pprint(matriz_jacobiana)

    # 4. Cálculo dos autovalores
    autovalores = matriz_jacobiana.eigenvals()
    print("\n--- Autovalores ---")
    for autovalor, multiplicidade in autovalores.items():
        print(f"λ = {float(autovalor):.5f} (multiplicidade: {multiplicidade})")

    # 5. Análise de estabilidade para sistema discreto (|λ| < 1)
    estavel = True
    print("\n--- Análise de Estabilidade ---")
    for autovalor in autovalores:
        modulo = float(sp.Abs(autovalor))
        if modulo >= 1:
            estavel = False
            print(f"Instável: |λ| = {modulo:.5f} >= 1")
        else:
            print(f"Estável: |λ| = {modulo:.5f} < 1")

    classificacao = "Estável" if estavel else "Instável"
    print(f"\nResultado final: O ponto fixo é {classificacao}.")


if __name__ == "__main__":
    analisar_sistema_dinamico()