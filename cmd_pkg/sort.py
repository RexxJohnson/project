import sys
import os
import errno


def sort(args):
    if len(args) == 1:
        print("need more arguments!")
    elif len(args) > 1:
        filename = args[1]
        file = open(filename, 'r')

        for line in file:
            word_list = line.split()

        word_list.sort()
        print(word_list)
