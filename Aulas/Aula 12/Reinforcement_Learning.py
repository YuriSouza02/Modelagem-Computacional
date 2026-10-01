"""Ambiente de Aprendizagem por Reforço: ShowerEnv.

Simulação do controlo contínuo de temperatura de um chuveiro através
da mistura de fluxos de água quente e fria.
"""

import gymnasium as gym

from gymnasium import spaces
import numpy as np


class ShowerEnv(gym.Env):
    """Ambiente Gymnasium para simulação do controlo de temperatura de um chuveiro."""

    def __init__(self, max_steps: int = 30):
        super().__init__()

        # Parâmetros térmicos do sistema (°C)
        self.T_hot = 60.0
        self.T_cold = 20.0
        self.T_target = 38.0
        self.max_steps = max_steps

        # Espaço de ação: fluxos contínuos de água [quente, fria] no intervalo [0.0, 1.0]
        self.action_space = spaces.Box(
            low=0.0, high=1.0, shape=(2,), dtype=np.float32
        )

        # Espaço de observação: temperatura atual da água (°C)
        self.observation_space = spaces.Box(
            low=0.0, high=100.0, shape=(1,), dtype=np.float32
        )

        self.state = np.array([self.T_cold], dtype=np.float32)
        self.current_step = 0

    def step(self, action: np.ndarray):
        self.current_step += 1

        # Adição de ruído estocástico à ação das válvulas
        noise = np.random.uniform(low=0.0, high=0.1, size=2)
        noisy_action = np.clip(action + noise, 0.0, 1.0)
        f_hot, f_cold = noisy_action
        total_flow = f_hot + f_cold

        # Cálculo da temperatura resultante da mistura
        if total_flow > 0:
            t_mix = (f_hot * self.T_hot + f_cold * self.T_cold) / total_flow
        else:
            t_mix = float(self.state[0])

        self.state = np.array([t_mix], dtype=np.float32)

        # Recompensa baseada no desvio térmico e penalização do consumo de água
        reward = -(
            abs(t_mix - self.T_target) + 0.1 * (f_cold + f_hot) + f_hot
        )

        # Condições de término do episódio
        temperature_reached = abs(t_mix - self.T_target) < 1.0
        terminated = temperature_reached
        truncated = self.current_step >= self.max_steps

        info = {
            "temperature_reached": bool(temperature_reached),
            "current_step": self.current_step,
            "error": abs(t_mix - self.T_target),
        }

        return self.state, reward, terminated, truncated, info

    def reset(self, seed: int | None = None, options: dict | None = None):
        super().reset(seed=seed)

        self.state = np.array([self.T_cold], dtype=np.float32)
        self.current_step = 0

        info = {"current_step": self.current_step}
        return self.state, info

    def render(self):
        print(
            f"🚿 Temperatura atual: {self.state[0]:.2f}°C | "
            f"🎯 Alvo: {self.T_target}°C | "
            f"Passo: {self.current_step}"
        )


def executar_simulacao(env: ShowerEnv, max_steps: int = 30) -> None:
    """Executa um episódio de teste com uma política heurística baseada em regras."""
    obs, info = env.reset(seed=42)
    done = False
    total_reward = 0.0

    while not done:
        temp_atual = obs[0]

        # Regra heurística simples para ajuste dos fluxos
        if temp_atual < 37.0:
            action = np.array([0.6, 0.4], dtype=np.float32)
        elif temp_atual > 39.0:
            action = np.array([0.4, 0.6], dtype=np.float32)
        else:
            action = np.array([0.0, 0.0], dtype=np.float32)

        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += float(reward)
        env.render()
        done = terminated or truncated

    print(f"\nEpisódio finalizado em {info['current_step']} passos.")
    print(f"Temperatura alcançada: {info['temperature_reached']}")
    print(f"Recompensa total acumulada: {total_reward:.2f}")


if __name__ == "__main__":
    ambiente = ShowerEnv(max_steps=30)
    executar_simulacao(ambiente)