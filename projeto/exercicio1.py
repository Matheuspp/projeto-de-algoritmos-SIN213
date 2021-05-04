import time

def selection_sort(entry):
    for i in range(len(entry)):
        min_idx = i
        for j in range(i+1, len(entry)):
            if entry[min_idx] > entry[j]:
                min_idx = j
                
        entry[i], entry[min_idx] = entry[min_idx], entry[i]

    return entry

def insertion_sort(entry):
    for i in range(1, len(entry)):
        key = entry[i]
        j = i-1
        while j >=0 and key < entry[j] :
            entry[j+1] = entry[j]
            j -= 1
            entry[j+1] = key

    return entry

def shell_sort(entry):
    n = len(entry)
    gap = int(n/2)
    print(gap)
    print(n)

    while gap > 0:  
        for i in range(gap,n):
            temp = entry[i]
            j = i
            while  j >= gap and entry[j-gap] >temp:
                entry[j] = entry[j-gap]
                j -= gap
            entry[j] = temp
        gap /= 2
        gap = int(gap)

    return entry

def merge(entry):
    for k in range(left, right + 1):
        aux[k] = entry[k]
    i = left
    j = middle + 1
    for k in range(left, right + 1):
        if i > middle:
            entry[k] = aux[j]
            j += 1
        elif j > right:
            entry[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            entry[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1

def merge_sort(entry, aux, left, right):
    if right <= left:
        return
    middle = (left + right) // 2

    # Ordena a primeira metade do arranjo.
    merge_sort(entry, aux, left, right)(A, aux, left, middle)

    # Ordena a segunda metade do arranjo.
    merge_sort(entry, aux, left, right)(A, aux, middle + 1, right)

    # Combina as duas metades ordenadas anteriormente.
    merge(A, aux, left, middle, right)


def read_data(path, entry_size=10, mode='random'):

    with open(f'{path}/entrada{entry_size}.txt', 'r') as fp:
        data = fp.read()

    data = [int(i) for i in data if i != '\n']
    
    if mode == 'crescente':
        return sorted(data)
    elif mode == 'decrescente':
        return sorted(data, reverse=True)
    else:
        return data


if __name__ in "__main__":
    # ### reading entries
    result_dict = {'selection_sort':{}, 'insertion_sort':{},
                   'shell_sort': {}, 'merge_sort':{}}

    entries = [10]
    modes = ['random', 'crescente', 'decrescente']

    for key, values in result_dict.items():
        for mode in modes:
            result_dict[key][mode] = []

    # ###  executando experimentos
    for mode in modes:
        for entry in entries:
            data = read_data('ArquivosOrdenacao/', entry_size=entry, mode=mode)
            
            # ### selection_sort sort algorithm
            tic = time.time()
            data_new = selection_sort(data)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['selection_sort'][mode].append(ex_time)

            # ### insertion_sort sort algorithm
            tic = time.time()
            data_new = insertion_sort(data)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['insertion_sort'][mode].append(ex_time)

            # ### shell_sort sort algorithm
            tic = time.time()
            data_new = shell_sort(data)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['shell_sort'][mode].append(ex_time)

            # ### merge sort algorithm
            #aux = [0] * len(data)
            tic = time.time()
            #merge_sort(data, aux, 0, len(data)-1)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['merge_sort'][mode].append(ex_time)
            

    print(result_dict)
    aux = [0] * len(data)
    #merge_sort(data, aux, 0, len(data)-1)
    