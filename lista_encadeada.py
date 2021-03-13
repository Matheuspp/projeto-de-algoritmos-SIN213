# ### lista encadeada simples 

class Node:
    """Nó de uma estrutura de dados encadeada simples"""
    def __init__(self, dado=0, proximo_no=None):
        self.dado = dado
        self.proximo = proximo_no

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    """Define o head que irá apontar para o inicio da lista
       encadeada simples
    """
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

def insert(lista, dado):
    # ### cria um novo no para inserir o dado
    novo = Node(dado)

    # ### o novo node criado será o primeiro (Head)
    novo.proximo = lista.head

    # ### o head da lista apontará para o novo node
    lista.head = novo


def main():


if __name__ in "__main__":
    main()


