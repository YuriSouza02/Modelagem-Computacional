import os
import cv2
import gym
import matplotlib.pyplot as plt
import numpy as np
from pyvirtualdisplay import Display
from tqdm import tqdm


# ==========================================
# POLÍTICA DE CONTROLO DO AGENTE
# ==========================================

def politica_heuristica(state: np.ndarray) -> float:
    """
    Define a ação contínua para o ambiente MountainCarContinuous-v0.
    Retorna um valor no intervalo [-1.0, 1.0] com base na posição e velocidade.
    """
    cart_pos, cart_vel = state[0], state[1]

    if -0.6 < cart_pos < 0.3:
        return 1.0 if cart_vel > 0 else -1.0
    return 1.0 if cart_vel > 0 else 0.0


# ==========================================
# EXECUÇÃO E GRAVAÇÃO DE VÍDEO
# ==========================================

def guardar_video(frames: list, caminho_saida: str = "video.mp4", fps: int = 25) -> None:
    """Converte a lista de frames RGB num ficheiro de vídeo MP4."""
    if not frames:
        return

    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(caminho_saida, fourcc, fps, (width, height))

    for frame in frames:
        video.write(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    video.release()


def executar_episodio(env, politica, gravar_video: bool = False, caminho_video: str = "video.mp4") -> float:
    """Executa um único episódio do ambiente e grava opcionalmente a simulação."""
    state = env.reset()
    done = False
    rewards = []
    frames = []

    while not done:
        if gravar_video:
            frames.append(env.render(mode="rgb_array"))

        action = politica(state)
        state, reward, done, _ = env.step(np.array([action]))
        rewards.append(reward)

    if gravar_video and frames:
        guardar_video(frames, caminho_video)

    return sum(rewards)


def avaliar_politica(env, politica, num_episodios: int = 500) -> list:
    """Avalia o desempenho de uma política ao longo de múltiplos episódios."""
    total_rewards = []

    for _ in tqdm(range(num_episodios), desc="A avaliar política"):
        state = env.reset()
        done = False
        recompensa_acumulada = 0.0

        while not done:
            action = politica(state)
            state, reward, done, _ = env.step(np.array([action]))
            recompensa_acumulada += reward

        total_rewards.append(recompensa_acumulada)

    return total_rewards


# ==========================================
# FLUXO PRINCIPAL
# ==========================================

if __name__ == "__main__":
    # Inicialização do ecrã virtual para ambientes sem interface gráfica física
    display = Display(visible=0, size=(1024, 768))
    display.start()

    env = gym.make("MountainCarContinuous-v0")

    # 1. Execução de episódio de teste com gravação de vídeo
    recompensa_teste = executar_episodio(
        env,
        politica_heuristica,
        gravar_video=True,
        caminho_video="video.mp4"
    )
    print(f"Recompensa obtida no episódio de teste: {recompensa_teste:.2f}")

    # 2. Avaliação de desempenho ao longo de 500 episódios
    num_eps = 500
    recompensas = avaliar_politica(env, politica_heuristica, num_episodios=num_eps)

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
    display.stop()