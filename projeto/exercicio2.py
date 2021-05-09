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


def get_encoded_text(huffman_code, text):
		encoded_text = ""
		for character in text:
			encoded_text += huffman_code[character]
		return encoded_text


def pad_encoded_text(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
        encoded_text += "0"

    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text


def get_byte_array(padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i+8]
        b.append(int(byte, 2))
    return b

def write_dvz(header, huffman_code, string, text_number=1):
    with open(f'compressed_{text_number}.dvz', 'wb') as output:			
        #output.write(bytes(''.join(header).encode()))
        #output.write(bytes('\n'.encode()))
        encoded_text = get_encoded_text(huffman_code, string)
        padded_encoded_text = pad_encoded_text(encoded_text)

        b = get_byte_array(padded_encoded_text)
        output.write(bytes(b))
    

def read_dvz(text_number=1):

    #with open(f'compressed_{text_number}.dvz', 'rb') as file:
    #    data = file.readlines()        
    #    cout = len(data[0])
    #    tree = data[0]

        
    with open(f'compressed_{text_number}.dvz', 'rb') as file:
        bit_string = ""

        byte = file.read(1)
        #for i in range(cout+1):
        #    file.read(1)

        while(byte != ""):
            if len(byte) == 0:
                break
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

    return bit_string
                 

def compress(path):
    maps = []
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
        maps.append(huffman_code)

        print(f'compressing file {i} ...')
        header = []

        for (char, freq) in frequency:
            #print(' %-4r |%12s' % (char, huffman_code[char]))
            pass

        for key, values in huffman_code.items():
            header.append(values)
            header.append(key)

        # ### saving .dvz extension 
        write_dvz(header, huffman_code, string, i)
        #print(huffman_code)

    return maps

def remove_padding(padded_encoded_text):

    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)

    padded_encoded_text = padded_encoded_text[8:] 
    encoded_text = padded_encoded_text[:-1*extra_padding]

    return encoded_text

def decode_text(encoded_text, mapping):
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if(current_code in mapping):
            character = mapping[current_code]
            decoded_text += character
            current_code = ""

    return decoded_text

def decompress(maps):

    for idx in range(1, 6):
        mapping = {}
        for key, values in maps[idx-1].items():
            mapping[values] = key

        bit_string = read_dvz(idx)

        #key = ''
        #value = ''
        #mapp = {}
        #for i in tree:

        #    if chr(i) == '1' or chr(i) == '0':
        #        key += chr(i)
        #    else:
        #        value += chr(i)
        #        mapp[key] = value

        #        key = ''
        #        value = ''

        encoded_text = remove_padding(bit_string)

        decompressed_text = decode_text(encoded_text, mapping)
        
        with open(f'decompressed_{idx}.txt', 'w') as fp:
            fp.write(decompressed_text)


if __name__ in '__main__':
    maps = compress('./ArquivosCompressor')
    
    decompress(maps)