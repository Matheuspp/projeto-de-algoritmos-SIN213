import template

class Node:
    def __init__(sefl, dado):
        self.dado = dado

def heapify(lista, n, i):
    # ### o primeiro elemento da raiz e considerado o maior
    maior = i
    esq = 2 * i + 1     # esquerda
    dir = 2 * i + 2     # direita
 
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
    for i in range( (n//2 - 1), -1, -1):
        heapify(lista, n, i)
 
    # ### extrai os elementos da heap
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]  # swap
        heapify(lista, i, 0)
 
 
if __name__ in "__main__":
    # ### carregando dados do template
    lista = template.arranjo

    heapSort(lista)
    n = len(lista)
    print("Sorted listaay is")
    for i in range(n):
        print("%d" % lista[i])