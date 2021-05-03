import time
import sys
sys.setrecursionlimit(10000000)

class Sort:
    def __init__(self, entry):
        self.entry = entry

    def selection(self):
        for i in range(len(self.entry)):
            min_idx = i
            for j in range(i+1, len(self.entry)):
                if self.entry[min_idx] > self.entry[j]:
                    min_idx = j
                    
            self.entry[i], self.entry[min_idx] = self.entry[min_idx], self.entry[i]

        return self.entry

    def insertion(self):
        for i in range(1, len(self.entry)):
            key = self.entry[i]
            j = i-1
            while j >=0 and key < self.entry[j] :
                self.entry[j+1] = self.entry[j]
                j -= 1
                self.entry[j+1] = key

        return self.entry

    def shell(self):
        n = len(self.entry)
        gap = int(n/2)
        print(gap)
        print(n)
  
        while gap > 0:  
            for i in range(gap,n):
                temp = self.entry[i]
                j = i
                while  j >= gap and self.entry[j-gap] >temp:
                    self.entry[j] = self.entry[j-gap]
                    j -= gap
                self.entry[j] = temp
            gap /= 2
            gap = int(gap)

        return self.entry

    def merge(self, entry):

        mid = len(entry)//2 
        L = entry[:mid]
        R = entry[mid:]

        # ### left
        self.merge(L)

        # ### right
        self.merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                entry[k] = L[i]
                i += 1
            else:
                entry[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            entry[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            entry[k] = R[j]
            j += 1
            k += 1

        return entry

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

def merge(entry):

    mid = len(entry)//2 
    L = entry[:mid]
    R = entry[mid:]

    # ### left
    merge(L)

    # ### right
    merge(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            entry[k] = L[i]
            i += 1
        else:
            entry[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        entry[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        entry[k] = R[j]
        j += 1
        k += 1

    return entry

if __name__ in "__main__":
    # ### reading entries
    result_dict = {'selection':{}, 'insertion':{},
                   'shell': {}, 'merge':{}}

    entries = [10]
    modes = ['random', 'crescente', 'decrescente']

    for key, values in result_dict.items():
        for mode in modes:
            result_dict[key][mode] = []

    # ###  executando experimentos
    for mode in modes:
        for entry in entries:
            data = read_data('ArquivosOrdenacao/', entry_size=entry, mode=mode)

            sort_by = Sort(data)
            
            # ### selection sort algorithm
            tic = time.time()
            data_new = sort_by.selection()
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['selection'][mode].append(ex_time)

            # ### insertion sort algorithm
            tic = time.time()
            data_new = sort_by.insertion()
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['insertion'][mode].append(ex_time)

            # ### shell sort algorithm
            tic = time.time()
            data_new = sort_by.shell()
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['shell'][mode].append(ex_time)

            # ### merge sort algorithm
            tic = time.time()
            data_new = merge(data)
            tac = time.time()            
            ex_time = abs(tac - tic)
            result_dict['merge'][mode].append(ex_time)

    print(result_dict)