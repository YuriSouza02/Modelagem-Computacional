# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Tenta importar utilitários do Google Colab
try:
    from google.colab import files
    IN_COLAB = True
except ImportError:
    IN_COLAB = False


def carregar_dados():
    """Carrega o arquivo CSV via Colab upload ou caminho local."""
    if IN_COLAB:
        uploaded = files.upload()
        if not uploaded:
            raise FileNotFoundError("Nenhum arquivo foi carregado.")
        filename = next(iter(uploaded))
    else:
        filename = "dados.csv"  # Altere para o caminho do seu arquivo local

    # Leitura otimizada com pandas (utf-8-sig remove BOM automaticamente)
    df = pd.read_csv(
        filename,
        sep=';',
        encoding='utf-8-sig',
        header=0,
        names=['municipio', 'nota', 'presenca']
    )
    return df


def analisar_permutacao_e_ttest(df, municipio_a="GOIANIA", municipio_b="VITORIA", n_permutations=10_000):
    """Filtra os dados, executa o Teste t e a Simulação de Permutação com gráfico."""
    
    # 1. Filtragem de dados (Apenas presentes: presenca == 1)
    df_presentes = df[df['presenca'] == 1].copy()
    
    # Normalização dos textos e conversão de notas
    df_presentes['municipio'] = df_presentes['municipio'].astype(str).str.strip().str.upper()
    df_presentes['nota'] = pd.to_numeric(df_presentes['nota'], errors='coerce').fillna(0.0)

    # Separação dos grupos
    grupo_a = df_presentes[df_presentes['municipio'] == municipio_a]['nota'].values
    grupo_b = df_presentes[df_presentes['municipio'] == municipio_b]['nota'].values

    # Validação de amostras
    if len(grupo_a) == 0 or len(grupo_b) == 0:
        print(f"Erro: Dados insuficientes para comparação ({municipio_a}: {len(grupo_a)}, {municipio_b}: {len(grupo_b)}).")
        return

    print(f"Amostras carregadas -> {municipio_a}: {len(grupo_a)} | {municipio_b}: {len(grupo_b)}")

    # 2. Estatística observada: diferença absoluta das médias
    obs_diff = np.abs(np.mean(grupo_a) - np.mean(grupo_b))
    print(f"Diferença observada entre as médias: {obs_diff:.4f}")

    # 3. Teste t clássico (bilateral)
    t_stat, p_teorico = ttest_ind(grupo_a, grupo_b, equal_var=True)
    print(f"Teste t: Estatística = {t_stat:.4f} | p-valor = {p_teorico:.4f}")

    # 4. Teste de Permutação
    combined = np.concatenate([grupo_a, grupo_b])
    len_a = len(grupo_a)
    diffs = np.zeros(n_permutations)

    rng = np.random.default_rng()
    for i in range(n_permutations):
        rng.shuffle(combined)
        diffs[i] = np.abs(np.mean(combined[:len_a]) - np.mean(combined[len_a:]))

    # p-valor empírico
    p_empirico = np.mean(diffs >= obs_diff)
    print(f"Permutação: p-valor empírico = {p_empirico:.4f}")

    # 5. Visualização Gráfica
    plt.figure(figsize=(9, 5))
    plt.hist(diffs, bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
    plt.axvline(obs_diff, color='red', linestyle='--', linewidth=2, label=f'Dif. observada = {obs_diff:.2f}')
    plt.axvline(np.mean(diffs), color='blue', linestyle='--', linewidth=2, label=f'Dif. permutada (média) = {np.mean(diffs):.2f}')

    plt.title("Comparação: Teste de Permutação vs Teste t")
    plt.xlabel("Diferença média entre grupos")
    plt.ylabel("Frequência")
    plt.legend(loc='upper right')
    plt.grid(True)

    # Adiciona os p-valores na figura
    max_y = plt.ylim()[1]
    plt.text(0.02, max_y * 0.90, f"p-valor permutação = {p_empirico:.4f}", fontsize=10)
    plt.text(0.02, max_y * 0.85, f"p-valor t-teste      = {p_teorico:.4f}", fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    dados_df = carregar_dados()
    analisar_permutacao_e_ttest(dados_df)