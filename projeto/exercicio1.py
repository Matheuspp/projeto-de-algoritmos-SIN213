import time

class Sort:
    def __init__(self, entries):
        self.entries = entries

    def selection(self):
        pass
    def insertion(self):
        pass
    def shell(self):
        pass
    def merge(self):
        pass

def read_data(path, entry_size=10):

    with open(f'{path}/entrada{entry_size}.txt') as fp:
        data = fp.read()

    return data

if __name__ in "__main__":
    # ### reading entries
    result_dict = {'selection':{}, 'insertion':{},
                   'shell': {}, 'merge':{}}
                   
    entries = [10, 1000, 10000, 10000, 100000]
    data = read_data('ArquivosOrdenacao/')

    print(data)