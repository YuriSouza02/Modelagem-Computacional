# -*- coding: utf-8 -*-
"""
Modelagem Computacional - Aprendizagem por Reforço com OpenAI Gym (CartPole-v0)

Instalação de dependências no ambiente de sistema:
    pip install gym numpy matplotlib moviepy opencv-python pyvirtualdisplay tqdm
    apt-get install python-opengl xvfb -y
"""

import os
import cv2
import gym
import matplotlib.pyplot as plt
import numpy as np
from pyvirtualdisplay import Display
from tqdm import tqdm

# Iniciar ecrã virtual para suporte a rendering sem interface gráfica física
display = Display(visible=0, size=(1024, 768))
display.start()


# ==========================================
# POLÍTICAS DE CONTROLO DO AGENTE
# ==========================================

def politica_sempre_direita(state: np.ndarray) -> int:
    """Ação fixa: empurrar o carrinho sempre para a direita."""
    return 1


def politica_aleatoria(state: np.ndarray) -> int:
    """Ação aleatória com probabilidade uniforme."""
    return 1 if np.random.rand() >= 0.5 else 0


def politica_angulo_mastro(state: np.ndarray) -> int:
    """Ação baseada apenas no sinal do ângulo do mastro."""
    _, _, pole_ang, _ = state
    return 1 if pole_ang >= 0 else 0


def politica_velocidade_mastro(state: np.ndarray) -> int:
    """Ação baseada na velocidade angular do mastro."""
    _, _, _, pole_vel = state
    return 0 if pole_vel > 0 else 1


def politica_velocidade_e_angulo_v1(state: np.ndarray) -> int:
    """Ação baseada na combinação simultânea de ângulo e velocidade."""
    _, _, pole_ang, pole_vel = state
    return 1 if (pole_vel > 0 and pole_ang > 0) else 0


def politica_velocidade_e_angulo_v2(state: np.ndarray) -> int:
    """Ação baseada no produto do ângulo e da velocidade angular."""
    _, _, pole_ang, pole_vel = state
    return 1 if (pole_vel * pole_ang > 0) else 0


# ==========================================
# EXECUÇÃO E GRAVAÇÃO
# ==========================================

def guardar_video(frames: list, caminho_saida: str = "video.mp4", fps: int = 25) -> None:
    """Converte a lista de frames gravados num ficheiro de vídeo MP4."""
    if not frames:
        return
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(caminho_saida, fourcc, fps, (width, height))

    for frame in frames:
        video.write(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    video.release()


def executar_episodio(env, politica, gravar_video: bool = False, caminho_video: str = "video.mp4") -> float:
    """
    Executa um único episódio do ambiente segundo a política fornecida.
    Guarda opcionalmente o vídeo da simulação.
    """
    state = env.reset()
    done = False
    rewards = []
    frames = []

    while not done:
        if gravar_video:
            frames.append(env.render(mode="rgb_array"))

        action = politica(state)
        state, reward, done, _ = env.step(action)
        rewards.append(reward)

    if gravar_video and frames:
        guardar_video(frames, caminho_video)

    return sum(rewards)


def avaliar_politica(env, politica, num_episodios: int = 500) -> list:
    """Avalia o Desempenho de uma política ao longo de múltiplos episódios."""
    total_rewards = []

    for _ in tqdm(range(num_episodios), desc="A avaliar política"):
        state = env.reset()
        done = False
        recompensa_acumulada = 0.0

        while not done:
            action = politica(state)
            state, reward, done, _ = env.step(action)
            recompensa_acumulada += reward

        total_rewards.append(recompensa_acumulada)

    return total_rewards


# ==========================================
# FLUXO PRINCIPAL
# ==========================================

if __name__ == "__main__":
    env = gym.make("CartPole-v0")

    # 1. Teste de execução individual com gravação de vídeo
    print("A executar episódio de demonstração...")
    recompensa_teste = executar_episodio(
        env,
        politica_velocidade_e_angulo_v1,
        gravar_video=True,
        caminho_video="video.mp4"
    )
    print(f"Recompensa obtida no episódio de teste: {recompensa_teste}")

    # 2. Avaliação de desempenho da política ao longo de 500 episódios
    num_eps = 500
    recompensas = avaliar_politica(env, politica_velocidade_e_angulo_v2, num_episodios=num_eps)

    # 3. Apresentação dos resultados estatísticos
    media = np.mean(recompensas)
    desvio_padrao = np.std(recompensas)

    plt.figure(figsize=(8, 5))
    plt.hist(recompensas, bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Distribuição de Recompensas ({num_eps} Episódios)\nMédia: {media:.2f} | Desvio Padrão: {desvio_padrao:.2f}")
    plt.xlabel("Recompensa Total")
    plt.ylabel("Frequência")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    env.close()