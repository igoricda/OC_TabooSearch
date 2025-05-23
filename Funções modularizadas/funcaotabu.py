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
        #print(f"Iteração {interacoes}: Melhor Custo = {melhor_custo}, Custo Atual = {custon}")

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
