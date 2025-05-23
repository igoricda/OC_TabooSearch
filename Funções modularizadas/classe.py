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
