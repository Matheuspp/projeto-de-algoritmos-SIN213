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
"""
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

"""

# Iterative Merge sort (Bottom Up)

# Iterative mergesort function to
# sort arr[0...n-1]
def mergeSort(a):
	
	current_size = 1
	
	# Outer loop for traversing Each
	# sub array of current_size
	while current_size < len(a) - 1:
		
		left = 0
		# Inner loop for merge call
		# in a sub array
		# Each complete Iteration sorts
		# the iterating sub array
		while left < len(a)-1:
			
			# mid index = left index of
			# sub array + current sub
			# array size - 1
			mid = min((left + current_size - 1),(len(a)-1))
			
			# (False result,True result)
			# [Condition] Can use current_size
			# if 2 * current_size < len(a)-1
			# else len(a)-1
			right = ((2 * current_size + left - 1,
					len(a) - 1)[2 * current_size
						+ left - 1 > len(a)-1])
							
			# Merge call for each sub array
			merge(a, left, mid, right)
			left = left + current_size*2
			
		# Increasing sub array size by
		# multiple of 2
		current_size = 2 * current_size


# Merge Function
def merge(a, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * n1
	R = [0] * n2
	for i in range(0, n1):
		L[i] = a[l + i]
	for i in range(0, n2):
		R[i] = a[m + i + 1]

	i, j, k = 0, 0, l
	while i < n1 and j < n2:
		if L[i] > R[j]:
			a[k] = R[j]
			j += 1
		else:
			a[k] = L[i]
			i += 1
		k += 1

	while i < n1:
		a[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		a[k] = R[j]
		j += 1
		k += 1


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
            mergeSort(data)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['merge_sort'][mode].append(ex_time)
            

    print(result_dict)
    with open('testes.txt', 'a+') as fp:
        fp.write(str(result_dict))
    