import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):

    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_huff_tree_02(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 13)
        self.assertEqual(hufftree.char, 32)
        left = hufftree.left
        self.assertEqual(left.freq, 6)
        self.assertEqual(left.char, 32)
        right = hufftree.right
        self.assertEqual(right.freq, 7)
        self.assertEqual(right.char, 97)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_encode(self):
        huffman_decode("file2_soln.txt", "file2_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_encode.txt file2.txt", shell = True)
        self.assertEqual(err, 0)

    def test_encode_02(self):
        huffman_decode("file1_soln.txt", "file1_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_encode.txt file1.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_encode(self):
        huffman_decode("multiline_soln.txt", "multiline_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_encode.txt multiline.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_encode(self):
        huffman_encode("single.txt", "single_out.txt")
        huffman_decode("single_out.txt", "single_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb single_encode.txt single.txt", shell = True)
        self.assertEqual(err, 0)

    def test_05_encode(self):
        huffman_encode("empty.txt", "empty_out.txt")
        huffman_decode("empty_out.txt", "empty_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_encode.txt empty.txt", shell = True)
        self.assertEqual(err, 0)

    def test_06_encode(self):
        huffman_encode("ye.txt", "ye_out.txt")
        huffman_decode("ye_out.txt", "ye_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb ye_encode.txt ye.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07_encode(self):
        huffman_decode("declaration_soln.txt", "declaration_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_encode.txt declaration.txt", shell = True)
        self.assertEqual(err, 0)

    def test_08_encode(self):
        huffman_encode("war.txt", "war_out.txt")
        huffman_decode("war_out.txt", "war_encode.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb war_encode.txt war.txt", shell = True)
        self.assertEqual(err, 0)



if __name__ == '__main__': 
   unittest.main()
