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
