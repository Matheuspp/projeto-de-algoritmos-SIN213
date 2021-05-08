# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def read_data(path, entry=1):

    with open(f'{path}/Compressor_{entry}.txt', 'r') as fp:
        data = fp.read()

    return data

def cal_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    return frequency

def save_dvz(tree_info, huffman_code=None, text_number=1):
    with open(f'compressed_{text_number}.dvz', 'w') as fp:
        fp.write(huffman_code)

if __name__ in '__main__':
    
    for i in range(1, 6):
         string = read_data('./ArquivosCompressor', entry=i)

    frequency = cal_frequency(string)
    nodes = frequency
    print(frequency)

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffman_code = huffman_code_tree(nodes[0][0])

    # ### saving .dvz extension 
    #save_dvz(None, huffman_code=huffman_code)
    print('----------------------')
    for (char, freq) in frequency:
        print(' %-4r |%12s' % (char, huffman_code[char]))