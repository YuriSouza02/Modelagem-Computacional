import time
import matplotlib.pyplot as plt

# Gerador Congruente Linear (LCG)
def lcg_random(quantidade, seed=None):
    if seed is None:
        seed = int(time.time() * 1000)
    a = 7**5         # 16807
    c = 2**31 - 1    # 2147483647
    
    numeros = []
    estado = seed
    for _ in range(quantidade):
        estado = (a * estado) % c
        numeros.append(estado / c)
    return numeros

# Inversão de distribuição acumulada para o atraso
def AtrasoSemanal(x):
    if x <= 0.3:
        return 1
    elif x <= 0.7:
        return 2
    else:
        return 3

# Inversão de distribuição acumulada para a demanda diária
def DemandaDiaria(x):
    if x <= 0.05:
        return 25
    elif x <= 0.15:
        return 30
    elif x <= 0.35:
        return 35
    elif x <= 0.65:
        return 40
    elif x <= 0.85:
        return 45
    elif x <= 0.95:
        return 50
    else:
        return 55

# Parâmetros da simulação
semanas = 52
custoPneu = 100        # Preço de venda de cada pneu
custoFalta = 80        # Multa por pneu não atendido
custoEstoque = 5       # Custo diário por pneu em estoque
recarga = 240          # Lote de reposição enviado pelo fabricante
estoque = 0
lucro = 0
atrasoPassado = 0

# Geramos uma sequência de números aleatórios suficiente para a simulação
aleatorios = lcg_random(semanas * 10)
rnd_idx = 0

Lucro_list, DemandaSemanal_list, DemandaDia_list, Estoque_list = [], [], [], []

for i in range(semanas):
    atrasoAtual = AtrasoSemanal(aleatorios[rnd_idx])
    rnd_idx += 1
    
    diasSemEntrega = 6 + atrasoAtual - atrasoPassado
    estoque += recarga
    
    for _ in range(diasSemEntrega):
        demanda = DemandaDiaria(aleatorios[rnd_idx])
        rnd_idx += 1
        
        if estoque < demanda:
            lucro += estoque * custoPneu
            lucro -= (demanda - estoque) * custoFalta
            estoque = 0
        else:
            lucro += demanda * custoPneu
            estoque -= demanda
            lucro -= estoque * custoEstoque
            
        Lucro_list.append(lucro)
        Estoque_list.append(estoque)
        DemandaDia_list.append(demanda)
        
    DemandaSemanal_list.append(sum(DemandaDia_list))
    DemandaDia_list = []
    atrasoPassado = atrasoAtual

media_demanda = sum(DemandaSemanal_list) / len(DemandaSemanal_list)
print(f"Demanda semanal média no período de {semanas} semanas: {media_demanda:.2f}\n")

plt.figure(figsize=(10, 4))
plt.plot(Lucro_list, 'r-.', label='Lucro Acumulado (diário)')
plt.ylabel('Valor ($)')
plt.xlabel('Dias')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(Estoque_list, 'b-.', label='Estoque (diário)')
plt.ylabel('Unidades')
plt.xlabel('Dias')
plt.legend()
plt.grid(True)
plt.show()