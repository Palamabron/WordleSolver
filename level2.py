from math import log2
import time
import numpy as np
import PySimpleGUI as sg

from ternary import ternary
from level1 import not_in_word_letters, misplaced_letters, correct_letters


def sort(value, wordsList):
    bitsValue = np.array(value)
    wordsList = np.array(wordsList)
    indexes = bitsValue.argsort()
    wordsList = wordsList[indexes]
    bitsValue = bitsValue[indexes]
    return wordsList, bitsValue


def writeToFile(bitsValue, wordsList):
    wordsList, bitsValue = sort(bitsValue, wordsList)
    with open('turn2bestWord.txt', 'w') as f:
        for i in range(len(wordsList)):
            tmp = ""
            for el in wordsList[i]:
                tmp += el
            if bitsValue[i] > 0:
                f.write(str(tmp) + ": " + str(bitsValue[i]) + "\n")


def updateProgress(window, key, progress):
    window[key].update("Progress" + str(progress))


# _ _ _ _ _
# 0 -> wrong, 1 -> misplaced, 2 -> correct
def evaluate(wordsList, possibleWords):
    bitsValues = []
    iteration = 1
    quater, half, threeForth = len(possibleWords) // 4, len(possibleWords) // 2, (len(possibleWords) * 3) // 4
    for oneWord in possibleWords:
        # print(iteration, end=": ")
        iteration += 1
        result = wordsList
        # wordSet = set(oneWord)
        # if len(wordSet) == 5:
        wordDistribution = []
        if quater == iteration or half == iteration or threeForth == iteration:
            print("#", end="")
        for i in range(243):  # 3 ^ 5
            combination = ternary(i)
            for j in range(5 - len(combination)):
                combination = "".join(['0', combination])
            missed, misplaced, correct = [], [], []
            missedChars = []
            misplacedChars, correctChars = ['_'] * 5, ['_'] * 5
            for j in range(len(combination)):
                if combination[j] == '0':
                    missed.append(j)
                elif combination[j] == '1':
                    misplaced.append(j)
                elif combination[j] == '2':
                    correct.append(j)
            if len(missed) > 0:
                for el in missed:
                    missedChars.append(oneWord[el])
                missedChars = ''.join(missedChars)
                result = not_in_word_letters(missedChars, result)
            if len(misplaced) > 0 and len(result) > 1:
                for j in misplaced:
                    misplacedChars[j] = oneWord[j]
                result = misplaced_letters(misplacedChars, result)
            if len(correct) > 0 and len(result) > 1:
                for j in correct:
                    correctChars[j] = oneWord[j]
                result = correct_letters(correctChars, result)
            # wzór: (len(result)/len(wordsList))*log2(len(wordsList) / len(result)
            if len(result) == 0:
                wordDistribution.append(0)
            else:
                px = len(result) / len(wordsList)
                wordDistribution.append(round(-log2(px) * px, 6))
            result = wordsList
        bitsValues.append(round(sum(wordDistribution), 4))
        # print(time.time())

    return bitsValues


def main():
    with open("D:\\Programming\\wordleSolver\\possible_words.txt") as file1:
        words = file1.read()
    with open("D:\\Programming\\wordleSolver\\turn2.txt") as file2:
        filtered_words = file2.read()
    words = words.split('\n')
    filtered_words = filtered_words.split('\n')
    filtered_words_final = []
    words_final = []
    tmp = []
    for word in words:
        for char in word:
            tmp.append(char)
        words_final.append(tmp)
        tmp = []
    for word in filtered_words:
        for char in word:
            tmp.append(char)
        filtered_words_final.append(tmp)
        tmp = []
    filtered_words_final = filtered_words_final[:-1]
    values = evaluate(filtered_words_final, words_final)
    bitsValue, wordsList = sort(values, words_final)
    # print(wordsList[:-10])
    # print(bitsValue[:-10])
    print('Best word is: ' + str(wordsList[-1]) + ' with value ' + str(bitsValue[-1]))
    writeToFile(values, words_final)
