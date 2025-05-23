import random
import time
import matplotlib.pyplot as plt
import sys

def tabu_search(size, matriz, solucao_inicial, max_interacoes, tabu):
    melhor_solucao = solucao_inicial
    vizinho = solucao_inicial
    melhor_custo = calcular_custo(melhor_solucao, matriz, size)
    custos = []  # Lista para armazenar a evolução do custo atual
    melhores_custos = []  # Lista para armazenar a evolução do melhor custo
    interacoes = 0

    while interacoes < max_interacoes:
        vizinho = gerar_vizinho(vizinho, tabu, matriz)
        interacoes += 1

        custon = calcular_custo(vizinho, matriz, size)
        custos.append(custon)
        if custon < melhor_custo:
            melhor_custo = custon
            melhor_solucao = vizinho
        melhores_custos.append(melhor_custo)
        print(f"Iteração {interacoes}: Melhor Custo = {melhor_custo}, Custo Atual = {custon}")

    # Gerar gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(custos)), custos, label='Custo Atual', color='blue')
    plt.plot(range(len(melhores_custos)), melhores_custos, label='Melhor Custo', color='red', linestyle='--')
    plt.xlabel("Iterações")
    plt.ylabel("Custo")
    plt.title("Evolução do Custo ao Longo das Iterações")
    plt.legend()
    plt.savefig("evolucao_custo.png")
    #plt.show()

    return melhor_solucao, melhor_custo


def verificar_validade(solucao, matriz):
    size = len(solucao)
    for i in range(1, size):
            if matriz[solucao[i] - 1][solucao[i-1] - 1] <= 0:
                #print(matriz[solucao[i] - 1][solucao[i-1] - 1], solucao[i], solucao[i-1])
                return True #True para invalido
    return False
    
def gerar_vizinho(solucao, tabu, matriz):
    size = len(solucao)
    melhor_solucao = []
    melhor_custo = float('inf')
    melhor_troca = None

    for i in range(1, size - 1):
        for j in range(i + 1, size - 1):
            vizinho = solucao.copy()
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]  # Trocar as cidades

            # Checar se é tabu
            if ([vizinho[i], vizinho[j]] in tabu.lista_tabu) or ([vizinho[j], vizinho[i]] in tabu.lista_tabu):
                continue

            # Checar validade
            if verificar_validade(vizinho, matriz):
                continue

            # Calcular custo do vizinho
            valor = calcular_custo(vizinho, matriz, size)

            # Atualiza melhor vizinho
            if valor < melhor_custo:
                melhor_custo = valor
                melhor_solucao = vizinho
                melhor_troca = [solucao[i], solucao[j]]  # Guardar a troca

    # Adicionar a melhor troca a lista tabu
    if melhor_troca:
        tabu.adicionar(melhor_troca)

    return melhor_solucao

def calcular_custo(solucao,matriz,size):
    custo_total = 0
    #print("New: ")
    #print(solucao)
    for i in range(len(solucao)- 1):
        #print(i)
        origem = solucao[i] - 1  # Converte o índice para base 0
        destino = solucao[i + 1] - 1  # Converte o índice para base 0
        #print(origem, destino)
        custo_total += matriz[origem][destino]
       # print(origem, destino, matriz[origem][destino], custo_total)

    return custo_total

def generate_dfs_solution(adj_matrix: list[list[float]]) -> list[int]:
    #DFS com backtracking
    num_cities = len(adj_matrix)
    visited = [False] * num_cities
    path = []

    def has_path_to_start(current_node: int) -> bool:
        return adj_matrix[current_node][0] > 0 #Checar se o nó tem como voltar ao primeiro

    def dfs(node: int) -> bool:

        visited[node] = True
        path.append(node)

        # Se visitou todos os nós, checar se pode voltar ao inicio
        if len(path) == num_cities:
            if has_path_to_start(node):
                return True
            # Senao, backtrack
            path.pop()
            visited[node] = False
            return False

        # Tentar todos os proximos nós possiveis
        for next_node in range(num_cities):
            if adj_matrix[node][next_node] > 0 and not visited[next_node]:
                if dfs(next_node):
                    return True

        # Se nao achar caminho valido, retornar
        path.pop()
        visited[node] = False
        return False

    # Iniciar DFS pelo nó 0 (0-index)
    if dfs(0):
        # se o caminho for valido, adicionar ao começo
        path.append(0)
        # Converter para 1-index
        return [x + 1 for x in path]
    else:
        raise ValueError("Nao existe caminho valido")

class ListaTabu:
    def __init__(self, tamanho):
        self.lista_tabu = []  # Inicializa a lista tabu
        self.tamanho = tamanho  # Define o tamanho máximo
        self.i = 0  # Inicia o índice

    def adicionar(self, vizinho):
        # Adiciona a troca à lista tabu com a interação
        if len(self.lista_tabu) < self.tamanho:
            self.lista_tabu.append(vizinho)
        else:
            self.lista_tabu.pop(0)
            self.lista_tabu.append(vizinho)
    def __str__(self):
        return f"Lista Tabu: {self.lista_tabu}"

# Para mudar o diretorio so mudar a parte "Entra x.txt"
print("Escreva a quantidade de cidades escolhida, de acordo com os grafos disponiveis:", end = " " )
num = input()
filename = 'Grafos Ponderados Não Direcionados/Entrada ' + num + '.txt'
arquivo = open(filename, 'r')
linhas = arquivo.readlines()
size = None
matriz = []

for i, linha in enumerate(linhas):
    linha = linha.strip()  # Remove espaços ou quebras de linha extras
    if i == 0:
        # A primeira linha é o tamanho da matriz
        size = int(linha)
    else:
        # As demais linhas contêm as coordenadas
        matriz.append(list(map(int, linha.split())))

solu_inicial = generate_dfs_solution(matriz)
print("Tamanho da lista Tabu:", end = " " )
tamanho = input()
tamanho = (int)(tamanho)
tabu =  ListaTabu(tamanho)
print("Número de iteracoes:", end = " " )
max_interacoes = input()
max_interacoes = (int)(max_interacoes)
melhor_solucao = solu_inicial
melhor_custo = calcular_custo(solu_inicial,matriz,size)
print("Solucao_inicial: ", solu_inicial, "Custo: ", melhor_custo)
melhor_solucao, melhor_custo = tabu_search(size, matriz, solu_inicial, max_interacoes, tabu)
custo_total = 0

"""
Teste se o caminho final é valido
for i in range(len(melhor_solucao)- 1):
        #print(i)
        origem = melhor_solucao[i] - 1  # Converte o índice para base 0
        destino = melhor_solucao[i + 1] - 1  # Converte o índice para base 0
        print(origem, destino)
        custo_total += matriz[origem][destino]
        print(origem, destino, matriz[origem][destino], custo_total)
"""
print("Melhor Solucao:", melhor_solucao)
print("Melhor Custo:", melhor_custo)



