import random

import numpy as np


# https://www.kaggle.com/rtatman/english-word-frequency
def writeFreqToList():
    with open("D:\\Programming\\wordleSolver\\wordsByFreqSorted.txt") as file:
        lines = file.read()
    lines = lines.split('\n')
    words = []
    for line in lines:
        line = line.split(': ')
        words.append(line[0])
    return words


def sortByFreq(words):
    values = []
    freqList = writeFreqToList()
    for i in range(len(words)):
        if words[i] in freqList:
            values.append(freqList.index(words[i]))
    words = np.array(words)
    values = np.array(values)
    indexes = values.argsort()
    words = words[indexes]
    values = values[indexes]
    return words


def getCommonWord(words):
    freqs = sortByFreq(words)
    tmp = None
    for j in range(len(freqs)):
        for i in range(len(words)):
            if freqs[j] == words[i]:
                tmp = words[i]
    if tmp is None:
        return words[0]
    else:
        return tmp
