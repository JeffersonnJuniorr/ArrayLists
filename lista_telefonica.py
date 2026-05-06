from array_list import ArrayList


# ======================================================================
#  Modelo de Contato
# ======================================================================

class Contato:
    """Representa um contato da lista telefônica."""

    def __init__(self, nome: str, telefone: str, email: str = ""):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        email_info = f" | E-mail: {self.email}" if self.email else ""
        return f"{self.nome:<25} | Tel: {self.telefone:<15}{email_info}"

    def __eq__(self, outro):
        if isinstance(outro, Contato):
            return self.nome.lower() == outro.nome.lower()
        return False


# ======================================================================
#  Lista Telefônica
# ======================================================================

class ListaTelefonica:
    """
    Lista telefônica implementada sobre a estrutura ArrayList.
    Suporta adicionar, remover, buscar, listar e atualizar contatos.
    """

    def __init__(self):
        self._contatos = ArrayList()   # <-- usa nossa estrutura de dados!

    # ------------------------------------------------------------------ #
    #  Operações CRUD                                                     #
    # ------------------------------------------------------------------ #

    def adicionar_contato(self, nome: str, telefone: str, email: str = ""):
        """Adiciona um novo contato ao final da lista."""
        if self._buscar_indice_por_nome(nome) != -1:
            print(f"  ✗  Contato '{nome}' já existe na agenda.")
            return False
        contato = Contato(nome, telefone, email)
        self._contatos.adicionar(contato)
        print(f"  ✓  Contato '{nome}' adicionado com sucesso.")
        return True

    def remover_contato(self, nome: str):
        """Remove um contato pelo nome."""
        indice = self._buscar_indice_por_nome(nome)
        if indice == -1:
            print(f"  ✗  Contato '{nome}' não encontrado.")
            return False
        self._contatos.remover(indice)
        print(f"  ✓  Contato '{nome}' removido com sucesso.")
        return True

    def buscar_contato(self, nome: str):
        """Busca e exibe um contato pelo nome (busca parcial)."""
        encontrados = ArrayList()
        nome_lower = nome.lower()
        for i in range(self._contatos.tamanho()):
            contato = self._contatos.obter(i)
            if nome_lower in contato.nome.lower():
                encontrados.adicionar(contato)

        if encontrados.esta_vazia():
            print(f"  ✗  Nenhum contato encontrado para '{nome}'.")
            return

        print(f"\n  Resultado(s) para '{nome}':")
        print("  " + "-" * 55)
        for i in range(encontrados.tamanho()):
            print(f"  {encontrados.obter(i)}")
        print()

    def atualizar_telefone(self, nome: str, novo_telefone: str):
        """Atualiza o telefone de um contato existente."""
        indice = self._buscar_indice_por_nome(nome)
        if indice == -1:
            print(f"  ✗  Contato '{nome}' não encontrado.")
            return False
        contato = self._contatos.obter(indice)
        contato.telefone = novo_telefone
        self._contatos.alterar(indice, contato)
        print(f"  ✓  Telefone de '{nome}' atualizado para {novo_telefone}.")
        return True

    def listar_todos(self):
        """Exibe todos os contatos em ordem de inserção."""
        if self._contatos.esta_vazia():
            print("  A lista telefônica está vazia.")
            return
        print(f"\n  {'AGENDA TELEFÔNICA':^55}")
        print("  " + "=" * 55)
        print(f"  {'Nome':<25} | {'Telefone':<15} | E-mail")
        print("  " + "-" * 55)
        for i in range(self._contatos.tamanho()):
            print(f"  {self._contatos.obter(i)}")
        print("  " + "=" * 55)
        print(f"  Total de contatos: {self._contatos.tamanho()}\n")

    def total_contatos(self):
        return self._contatos.tamanho()

    # ------------------------------------------------------------------ #
    #  Auxiliar interno                                                   #
    # ------------------------------------------------------------------ #

    def _buscar_indice_por_nome(self, nome: str) -> int:
        """Busca exata pelo nome (case-insensitive). Retorna índice ou -1."""
        nome_lower = nome.lower()
        for i in range(self._contatos.tamanho()):
            if self._contatos.obter(i).nome.lower() == nome_lower:
                return i
        return -1


# ======================================================================
#  Menu interativo (demonstração em terminal)
# ======================================================================

def menu():
    agenda = ListaTelefonica()

    # Dados iniciais de exemplo
    agenda.adicionar_contato("Ana Lima",       "(63) 99101-2233", "ana@email.com")
    agenda.adicionar_contato("Bruno Souza",    "(63) 98765-4321")
    agenda.adicionar_contato("Carla Mendes",   "(11) 91234-5678", "carla@email.com")
    agenda.adicionar_contato("Diego Ferreira", "(21) 99887-6655")
    agenda.adicionar_contato("Elena Costa",    "(63) 92233-4455", "elena@email.com")

    opcoes = {
        "1": "Listar todos os contatos",
        "2": "Adicionar contato",
        "3": "Buscar contato",
        "4": "Atualizar telefone",
        "5": "Remover contato",
        "0": "Sair",
    }

    while True:
        print("\n" + "=" * 40)
        print("       LISTA TELEFÔNICA - MENU")
        print("=" * 40)
        for chave, descricao in opcoes.items():
            print(f"  [{chave}] {descricao}")
        print("=" * 40)

        escolha = input("  Opção: ").strip()

        if escolha == "1":
            agenda.listar_todos()

        elif escolha == "2":
            nome = input("  Nome: ").strip()
            tel  = input("  Telefone: ").strip()
            mail = input("  E-mail (opcional): ").strip()
            agenda.adicionar_contato(nome, tel, mail)

        elif escolha == "3":
            nome = input("  Nome (ou parte dele): ").strip()
            agenda.buscar_contato(nome)

        elif escolha == "4":
            nome = input("  Nome do contato: ").strip()
            tel  = input("  Novo telefone: ").strip()
            agenda.atualizar_telefone(nome, tel)

        elif escolha == "5":
            nome = input("  Nome do contato a remover: ").strip()
            agenda.remover_contato(nome)

        elif escolha == "0":
            print("\n  Encerrando... Até logo!\n")
            break

        else:
            print("  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
