'''
    author: Matheus
    date: april 2021
'''

def pesquisa_binaria(arranjo, esquerda, direita, item):
    '''
       Uma impletação simples em python de uma busca binária recursiva
       complexidade: O(logn)
    '''
    if len(arranjo) == 0:
        return -1
    meio = esquerda + direita // 2
    
    if arranjo[meio] == item:
        return meio
    elif arranjo[meio] > item:
        return pesquisa_binaria(arranjo, meio-1, direita, item)
    elif arranjo[meio] < item:
        return pesquisa_binaria(arranjo, esquerda, meio+1, item)

if __name__ in '__main__':
    arranjo = range(0, 30)
    # ### tests
    test1 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 20)
    test2 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 2)
    test3 = pesquisa_binaria(arranjo, 0, len(arranjo)-1, 40)

    print(f'test1: {test1} test2: {test2} test3: {test3}')