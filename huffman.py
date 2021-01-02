class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq == b.freq:
        if a.char < b.char:
            return True
    return False

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    n = HuffmanNode(None, a.freq + b.freq)
    if a.char <= b.char:
        n.char = a.char
    else:
        n.char = b.char

    n.set_left(a)
    n.set_right(b)

    return n


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    store = [0] * 256
    f = open(filename, 'r')
    f1 = f.readlines()
    for i in f1:
        i = list(i)
        for j in i:
            store[ord(j)] += 1
    f.close()

    return store



def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    fleb = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            fleb.append(HuffmanNode(i, char_freq[i]))

    if len(fleb) == 1:
        return fleb[0]
    if len(fleb) == 0:
        return None

    for j in range(len(fleb)):
        minval = j
        for k in range(j, len(fleb)):
            if comes_before(fleb[k], fleb[j]):
                minval = k
                temp = fleb[k]
                fleb[k] = fleb[j]
                fleb[j] = temp

    while len(fleb) != 2:
        gud = combine(fleb[0], fleb[1])
        fleb.pop(0)
        fleb.pop(0)
        for i in range(len(fleb)):
            if i == len(fleb) - 1 and comes_before(fleb[i], gud):
                fleb.append(gud)
            elif comes_before(gud, fleb[i]):
                fleb.insert(i, gud)
                break
    gudlast = combine(fleb[0], fleb[1])
    fleb.pop(0)
    fleb.pop(0)
    fleb.append(gudlast)
    return fleb[0]



def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location"""

    codelist = [''] * 256
    code = ''

    if node is None:
        return codelist
    elif not(node.right or node.left):
        return codelist

    templist = create_code_help(node, code)
    for i in templist:
        i = i.split()
        idx = int(i[1])
        codelist[idx] = i[0]
    return codelist


def create_code_help(node, code):
    if not(node.left or node.right):
        return [code + ' ' + str(node.char)]
    return create_code_help(node.left, code + '0') + create_code_help(node.right, code + '1')



def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with aaabbbbcc, would return 97 3 98 4 99 2 """
    header = ''
    for i in range (len(freqs)):
        if freqs[i] != 0:
            header = header + str(i) + ' ' + str(freqs[i]) + ' '
    return header[:len(header) - 1]


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    freqlist = cnt_freq(in_file)
    hufftree = create_huff_tree(freqlist)
    codelist = create_code(hufftree)
    header = create_header(freqlist)
    f = open(in_file, 'r')
    g = open(out_file, 'w')

    if hufftree is None:
        g.close()
        f.close()
        return

    g.write(header + "\n")

    if not (hufftree.left or hufftree.right):
        g.close()
        f.close()
        return

    for i in f:
        i = list(i)
        for j in range(len(i)):
            i[j] = codelist[ord(i[j])]
        i = ''.join(i)
        g.write(i)

    f.close()
    g.close()

def parse_header(header):
    """Takes huffman encoded input file and parses the header to retrieve all ascii characters and
    their frequencies and returns a list of strings, each string containing the ascii character and
    the frequency"""
	
    finlist = [0] * 256

    header = header.split()

    for i in range(0,len(header),2):
        finlist[int(header[i])] = int(header[i+1])

    return finlist


def huffman_decode(in_file, out_file):

    f = open(in_file, 'r')
    g = open(out_file, 'w')

    temp = f.readline()

    freqlist = parse_header(temp)

    hufftree = create_huff_tree(freqlist)



    if hufftree is None:
        g.write('')
        f.close()
        g.close()
        return

    if not(hufftree.left or hufftree.right):
        for i in range(hufftree.freq):
            g.write(chr(hufftree.char))
        f.close()
        g.close()
        return

    for i in f:
        line = []
        geb = list(i)
        node = hufftree
        j = 0
        while j < len(geb):
            if not(node.left or node.right):
                line.append(chr(int(node.char)))
                node = hufftree
            elif geb[j] == '1':
                node = node.right
                j += 1
            elif geb[j] == '0':
                node = node.left
                j += 1
        line.append(chr(int(node.char)))
        line = ''.join(line)        
        g.write(line)

    f.close()
    g.close()

    
                

        





