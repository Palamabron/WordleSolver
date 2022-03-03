import random

import numpy as np


# https://www.kaggle.com/rtatman/english-word-frequency
def writeFreqToList():
    with open("D:\\Programming\\wordleSolver\\freqDb.txt") as file:
        lines = file.read()
    lines = lines.split('\n')
    words = []
    for line in lines:
        line = line.split(': ')
        words.append(line[0])
    return words


def sortByFreq(words):
    for i in range(len(words)):
        words[i] = "".join(words[i])
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
    best = None
    second = None
    for j in range(len(freqs)):
        for i in range(len(words)):
            if freqs[j] == words[i] and best is not None:
                second = words[i]
            if freqs[j] == words[i] and best is None:
                best = words[i]
            if best is not None and second is not None:
                break

    if best is None and len(words) > 1:
        return words[0], words[1]
    elif best is not None and len(words) == 1:
        return best, None
    elif best is None and len(words) == 1:
        return words[0], None
    elif best is not None and second is not None:
        return best, second
    else:
        return words[0], None
