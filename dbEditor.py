import math
import numpy as np


def importing():
    with open("D:\\Programming\\wordleSolver\\idk.txt") as file:
        lines = file.read()
    lines = lines.split('\n')
    file1 = open("dbFinal.txt", "w")
    for line in lines:
        line = line.split('\t')
        if len(line[1]) == 5:
            print(line[1] + ": " + str(int(int(round(float(line[2])) * 237))))
            file1.write(line[1] + ": " + str(int(round(float(line[2]) * 237))) + "\n")

    file1.close()


def addToDb():
    with open("D:\\Programming\\wordleSolver\\dbFinal.txt") as file:
        dbFinal = file.read()
    with open("D:\\Programming\\wordleSolver\\wordsByFreqSorted.txt") as file:
        wordsFreq = file.read()
    dbFinal = dbFinal.split('\n')
    wordsFreq = wordsFreq.split('\n')
    tmp = []
    result = []
    for i in range(len(wordsFreq)):
        wordsFreq[i] = wordsFreq[i].split(': ')
        tmp.append(wordsFreq[i][0])
        result.append(wordsFreq[i])
    for i in range(len(dbFinal)):
        dbFinal[i] = dbFinal[i].split(': ')
    for i in range(len(dbFinal)):
        if dbFinal[i][0] not in tmp:
            tmp.append(dbFinal[i][0])
            result.append(dbFinal[i])
    words = []
    values = []
    for i in range(len(result)):
        words.append(result[i][0])
        values.append(int(result[i][1]))
    words = np.array(words)
    values = np.array(values)
    indexes = values.argsort()
    words = words[indexes][::-1]
    values = values[indexes][::-1]

    freqDb = open("freqDb.txt", 'w')
    for i in range(len(words)):
        freqDb.write(words[i] + ": " + str(values[i]) + '\n')
    freqDb.close()

addToDb()
