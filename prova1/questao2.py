import template

# ###========================================
# ### Arvore binária de busca 
# ###========================================

class Node:
    def __init__(self, dado):

        self.ant = None
        self.prox = None
        self.dado = dado

    def inserir(self, dado):

        if self.dado:
            if dado < self.dado:
                if self.ant is None:
                    self.ant = Node(dado)
                else:
                    self.ant.inserir(dado)
            elif dado > self.dado:
                if self.prox is None:
                    self.prox = Node(dado)
                else:
                    self.prox.inserir(dado)
        else:
            self.dado = dado

# ### busca de uma chave na arvore recursivamente

    def busca(self, chave):
        if chave < self.dado:
            if self.ant is None:
                return f"{chave} não encontrado"
            return self.ant.busca(chave)
        elif chave > self.dado:
            if self.prox is None:
                return f"{chave} não encontrado"
            return self.prox.busca(chave)
        else:
            return f"{self.dado} encontrado"

    def imprimir(self):
        if self.ant:
            self.ant.imprimir()
        print(self.dado),
        if self.prox:
            self.prox.imprimir()

# ###========================================
# ### heapsort
# ###========================================

def heapify(lista, n, i):
    # ### o primeiro elemento da raiz e considerado o maior
    maior = i
    esq = 2*i+1     # esquerda
    dir = 2*i+2     # direita
 
    # ### max-heap: verifica se o filho é maior que o pai
    if esq < n and lista[maior] < lista[esq]:
        maior = esq
 
    if dir < n and lista[maior] < lista[dir]:
        maior = dir
 
    # ### faz a troca com a raiz quando necessário
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i] 
 
        # ### faz esse processo recursivamente
        heapify(lista, n, maior) 
 
def heapSort(lista):
    """ Ordena os elemento de uma uma maxheap"""
    n = len(lista)
 
    # ### constroi um maxheap.
    inicio = (n//2 - 1)
    
    for i in range(inicio , -1, -1):
        heapify(lista, n, i)
 
    # ### extrai os elementos da heap
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # swap
        heapify(lista, i, 0)
 
 
if __name__ in "__main__":
    # ### carregando dados do template
    lista = template.arranjo

    # ### heapsort
    heapSort(lista)
    n = len(lista)
    for i in range(n):
        pass
        #print(f"{lista[i]}")
    
    # ### arvore binária
    raiz = Node(lista[0])
    for item in lista[1:]:
        raiz.inserir(item)

    raiz.imprimir()
