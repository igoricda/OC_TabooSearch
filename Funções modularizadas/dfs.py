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
