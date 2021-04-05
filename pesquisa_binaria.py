'''
    author: Matheus
    date: april 2021
'''
import time

def pesquisa_binaria(arranjo, esquerda, direita, item):
    '''
       Uma impletação simples em python de uma busca binária recursiva
       complexidade: O(logn)
    '''
    
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    
    if arranjo[meio] == item:
        return meio
    elif arranjo[meio] > item:
        return pesquisa_binaria(arranjo, meio-1, direita, item)
    elif arranjo[meio] < item:
        return pesquisa_binaria(arranjo, esquerda, meio+1, item)

if __name__ in '__main__':
    arranjo = range(0, 100)
    # ### tests
    tic = time.time()
    test1 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 20)
    test2 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 400)
    test3 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 1001)
    toc = time.time()

    print(f'test1: {test1} test2: {test2} test3: {test3}')
    print(f'time: {abs(tic-toc)}')