def verificar_validade(solucao, matriz):
    size = len(solucao)
    for i in range(1, size):
            if matriz[solucao[i] - 1][solucao[i-1] - 1] <= 0:
                #print(matriz[solucao[i] - 1][solucao[i-1] - 1], solucao[i], solucao[i-1])
                return True #True para invalido
    return False
