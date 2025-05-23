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
