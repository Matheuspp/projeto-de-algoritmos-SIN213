'''
    author: Matheus
    date: april 2021
'''

def pesquisa_linear(arranjo, item):
    '''
       Uma impletação simples em python de uma busca sequencial
       complexidade: O(n)
    '''
    if len(arranjo) == 0:
        return None
    idx = 0
    for i in arranjo:
        if item == i:
            return idx
        idx += 1
    
    return -1

if __name__ in '__main__':
    arranjo = range(2, 30)
    # ### tests
    test1 = pesquisa_linear(arranjo, 3)
    test2 = pesquisa_linear(arranjo, 12)
    test3 = pesquisa_linear(arranjo, 34)

    print(f'test1: {test1} test2: {test2} test3: {test3}')