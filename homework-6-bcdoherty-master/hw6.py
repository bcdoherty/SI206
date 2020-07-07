import re
import unittest

def sumNums(fileName):
    file = open(fileName,"r")
    text = file.read()
    file.close()

    lst = re.findall(r'\d+', text)
    lst2 = []
    add = 0

    for x in range(len(lst)):
        num = int(lst[x])
        lst2.append(num)
    for x in range(len(lst2)):
        add = lst2[x] + add

    return add

def countWord(fileName, word):
    file = open(fileName, "r")
    text = file.read()
    file.close()

    text = text.lower()
    str1 = r'\b'+ word + r'\b'
    lst = re.findall(str1, text)

    return(len(lst))

def listURLs(fileName):
    file = open(fileName, "r")
    text = file.read()
    file.close()

    lst = re.findall(r'\bwww\..+\..+?\s', text)
    return(lst)


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
