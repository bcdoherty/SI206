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

add = sumNums("regex_sum_132198.txt")
print(add)
