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

def save_dvz(header, second_line=None, text_number=1):
    with open(f'compressed_{text_number}.dvz', 'w+') as fp:
        fp.write(''.join(header))
        
        fp.write('\n')
        fp.write(''.join(second_line))

def write_dvz(header, huffman_code, string, text_number=1):
    byte = ''
    byte_stack = ''
    for char in string:
        if len(byte) < 8:
            if len(byte_stack) != 0:
                byte += byte_stack
                byte_stack = ''
            else:
                byte += huffman_code[char]

        elif len(byte) > 8:
            byte_stack += byte[8:]
            byte = byte[0:8]
        else:
            # ### final string
            if char == string[-1]:
                if len(byte) < 8:
                    byte += '0'* (8 - len(byte))

                    with open(f'compressed_{text_number}.dvz', 'a+') as fp:
                        fp.write(byte)

                elif len(byte) > 8:
                    byte_stack += byte[8:]
                    byte = byte[0:8]

                    byte_stack += '0'* (8 - len(byte_stack))

                    with open(f'compressed_{text_number}.dvz', 'a+') as fp:
                        fp.write(byte)
                        fp.write(byte_stack)

            with open(f'compressed_{text_number}.dvz', 'a+') as fp:
                fp.write(byte)
                byte = ''
        

def compress(path):
    
    for i in range(1, 6):
        string = read_data(path, entry=i)

        frequency = cal_frequency(string)
        nodes = frequency
        #print(frequency)

        while len(nodes) > 1:
            (key1, c1) = nodes[-1]
            (key2, c2) = nodes[-2]
            nodes = nodes[:-2]
            node = NodeTree(key1, key2)
            nodes.append((node, c1 + c2))

            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

        huffman_code = huffman_code_tree(nodes[0][0])

        print('----------------------')
        print('  compressing ...')
        print('----------------------')
        header = [str(len(string))]
        second_line = []
        for (char, freq) in frequency:
            #print(' %-4r |%12s' % (char, huffman_code[char]))
            header.append(huffman_code[char])
            header.append(char)
            second_line.append(huffman_code[char])

        # ### saving .dvz extension 
        #save_dvz(header, second_line, text_number=i)
        write_dvz(header, huffman_code, string, i)
        print(huffman_code)
        #print(nodes[0][0].children())
        #print(nodes[0][0])



if __name__ in '__main__':
    compress('./ArquivosCompressor')