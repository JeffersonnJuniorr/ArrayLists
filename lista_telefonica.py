class ArrayList:


    CAPACIDADE_INICIAL = 4

    def __init__(self):
        self._capacidade = self.CAPACIDADE_INICIAL
        self._dados = [None] * self._capacidade
        self._tamanho = 0

    # ------------------------------------------------------------------ #
    #  Métodos principais                                                  #
    # ------------------------------------------------------------------ #

    def adicionar(self, elemento):
        """Adiciona um elemento ao final da lista."""
        self._garantir_capacidade()
        self._dados[self._tamanho] = elemento
        self._tamanho += 1

    def inserir(self, indice, elemento):
        """Insere um elemento em uma posição específica."""
        self._verificar_indice_insercao(indice)
        self._garantir_capacidade()
        # Desloca os elementos para a direita
        for i in range(self._tamanho, indice, -1):
            self._dados[i] = self._dados[i - 1]
        self._dados[indice] = elemento
        self._tamanho += 1

    def remover(self, indice):
        """Remove o elemento de uma posição e retorna seu valor."""
        self._verificar_indice(indice)
        elemento = self._dados[indice]
        # Desloca os elementos para a esquerda
        for i in range(indice, self._tamanho - 1):
            self._dados[i] = self._dados[i + 1]
        self._dados[self._tamanho - 1] = None
        self._tamanho -= 1
        return elemento

    def obter(self, indice):
        """Retorna o elemento de uma posição sem removê-lo."""
        self._verificar_indice(indice)
        return self._dados[indice]

    def alterar(self, indice, elemento):
        """Substitui o elemento de uma posição."""
        self._verificar_indice(indice)
        self._dados[indice] = elemento

    def buscar(self, elemento):
        """
        Busca linear: retorna o índice da primeira ocorrência
        ou -1 se não encontrado.
        """
        for i in range(self._tamanho):
            if self._dados[i] == elemento:
                return i
        return -1

    def tamanho(self):
        """Retorna a quantidade de elementos na lista."""
        return self._tamanho

    def esta_vazia(self):
        """Retorna True se a lista não tiver elementos."""
        return self._tamanho == 0

    def limpar(self):
        """Remove todos os elementos da lista."""
        self._capacidade = self.CAPACIDADE_INICIAL
        self._dados = [None] * self._capacidade
        self._tamanho = 0

    # ------------------------------------------------------------------ #
    #  Métodos auxiliares internos                                        #
    # ------------------------------------------------------------------ #

    def _garantir_capacidade(self):
        """Dobra a capacidade interna quando o array está cheio."""
        if self._tamanho == self._capacidade:
            nova_capacidade = self._capacidade * 2
            novo_array = [None] * nova_capacidade
            for i in range(self._tamanho):
                novo_array[i] = self._dados[i]
            self._dados = novo_array
            self._capacidade = nova_capacidade

    def _verificar_indice(self, indice):
        if indice < 0 or indice >= self._tamanho:
            raise IndexError(
                f"Índice {indice} inválido para lista de tamanho {self._tamanho}."
            )

    def _verificar_indice_insercao(self, indice):
        if indice < 0 or indice > self._tamanho:
            raise IndexError(
                f"Índice de inserção {indice} inválido para lista de tamanho {self._tamanho}."
            )

    # ------------------------------------------------------------------ #
    #  Representação textual                                              #
    # ------------------------------------------------------------------ #

    def __str__(self):
        elementos = [str(self._dados[i]) for i in range(self._tamanho)]
        return "[" + ", ".join(elementos) + "]"

    def __repr__(self):
        return f"ArrayList(tamanho={self._tamanho}, capacidade={self._capacidade})"
