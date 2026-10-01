# -*- coding: utf-8 -*-
"""Modelagem Computacional"""
import sympy as sp


def analisar_sistema_3d():
    # 1. Definição explícita dos símbolos do SymPy
    k_1, k_2, k_3, k_4, k_5, k_6, k_7, k_8, k_9 = sp.symbols(
        'k_1 k_2 k_3 k_4 k_5 k_6 k_7 k_8 k_9'
    )
    O, H, M = sp.symbols('O H M')

    # Dicionário de parâmetros numéricos utilizando os símbolos como chaves
    param_valores = {
        k_1: 0.01,  k_4: 0.001, k_8: 0.001,
        k_2: 0.01,  k_5: 0.001, k_9: 0.001,
        k_3: 100.0, k_6: 0.005, k_7: 0.05
    }

    # Vetor de estado u e sistema de equações F(u)
    u = sp.Matrix([O, H, M])
    F = sp.Matrix([
        (1 + k_1) * O - k_4 * O * H + k_9 * O * M,
        (1 + k_2) * H - k_5 * O * H + k_8 * H * M,
        (1 + k_3) * M - k_6 * O * M - k_7 * H * M
    ])

    # Sistema para determinação dos pontos fixos: u - F(u) = 0
    delta = u - F
    J = F.jacobian(u)

    # 2. Resolução algébrica dos pontos fixos
    solucoes = sp.solve(-delta, u, dict=True)
    print(f"Número de soluções (pontos fixos) encontradas: {len(solucoes)}")

    # 3. Análise de cada ponto fixo encontrado
    for idx, s in enumerate(solucoes, start=1):
        print("\n" + "=" * 80)
        print(f"SOLUÇÃO NÚMERO {idx}:")

        print("\n• Ponto Fixo Simbólico:")
        sp.pprint(s)

        # Substituição numérica no ponto fixo
        s_num = {var: val.subs(param_valores) for var, val in s.items()}
        print("\n• Ponto Fixo Numérico:")
        for var, val in s_num.items():
            print(f"  {var} = {float(val):.5f}")

        # Matriz Jacobiana avaliada no ponto fixo numérico
        J_ponto_num = J.subs(s).subs(param_valores)
        print("\n• Matriz Jacobiana Numérica no Ponto Fixo:")
        sp.pprint(J_ponto_num)

        # Cálculo e exibição dos autovalores da Jacobiana
        autovalores = J_ponto_num.eigenvals()
        print("\n• Autovalores da Matriz Jacobiana:")
        for autovalor, mult in autovalores.items():
            val_complex = complex(autovalor)
            modulo = abs(val_complex)
            print(f"  λ = {val_complex:.5f} | Módulo |λ| = {modulo:.5f} (mult: {mult})")


if __name__ == "__main__":
    analisar_sistema_3d()