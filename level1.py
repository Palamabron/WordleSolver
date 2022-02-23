import numpy as np


def writeToFile(wordsList):
    with open('turn2.txt', 'w') as f:
        for i in range(len(wordsList)):
            tmp = ""
            for el in wordsList[i]:
                tmp += el
            f.write(str(tmp) + "\n")


def correct_letters(fiveLetterList, words_list):
    result_list = []
    isGood = 1
    for word_list in words_list:
        for i in range(len(fiveLetterList)):
            if fiveLetterList[i] != '_':
                if word_list[i] != fiveLetterList[i]:
                    isGood = 0
        if isGood:
            result_list.append(word_list)
        else:
            isGood = 1

    return result_list


# ulepszyć
def misplaced_letters(fiveLetterList, words_list):
    result_list = []
    # .filter(lambda val: val != '_')
    chars = []
    charsIndex = []
    for i in range(len(fiveLetterList)):
        if fiveLetterList[i] != '_':
            chars.append(fiveLetterList[i])
            charsIndex.append(i)

    for word_list in words_list:
        isGood = 1
        if set(chars).issubset(word_list):
            for j in range(len(charsIndex)):
                if word_list[charsIndex[j]] == chars[j]:
                    isGood = 0
            if isGood:
                result_list.append(word_list)

    return result_list


def not_in_word_letters(chars, words_list):
    chars = list(chars)
    if not isinstance(words_list, list):
        words_list = list(words_list)
    result_list = []
    isGood = 1
    for word_list in words_list:
        for el in chars:
            if el in word_list:
                isGood = 0
                break
        if isGood:
            result_list.append(word_list)
        isGood = 1
    # print(result_list)
    return result_list


def evaluation(words_list):
    words_list = list(words_list)
    letter_freq = {'a': 8.157, 'b': 2.484, 'c': 3.349, 'd': 4.103, 'e': 10.453, 'f': 1.949, 'g': 2.359,
                   'h': 2.828, 'i': 5.531, 'j': 0.309, 'k': 2.071, 'l': 5.51, 'm': 2.929, 'n': 4.464,
                   'o': 6.653, 'p': 3.318, 'q': 0.184, 'r': 6.635, 's': 10.537, 't': 5.506, 'u': 3.783,
                   'v': 1.105, 'w': 1.754, 'x': 0.483, 'y': 3.078, 'z': 0.469}

    values = []
    for i in range(len(words_list)):
        value = 0
        for j in range(len(words_list[i])):
            value += letter_freq.get(words_list[i][j])
            if j == 0 and words_list[i][j] == 's':
                value += 15
            elif j == 0 and words_list[i][j] in ('a', 'b', 'c', 't', 'p', 'f'):
                value += 5
            elif j == 1 and words_list[i][j] in ('a', 'o', 'r', 'e', 'i', 'l', 'u', 'h'):
                value += 5
            elif j == 2 and words_list[i][j] in ('a', 'o', 'r', 'e', 'i', 'n', 'u'):
                value += 5
            elif j == 3 and words_list[i][j] in ('n', 's', 'a', 'l', 'i', 'r', 'c', 't', 'o'):
                value += 5
            elif j == 3 and words_list[i][j] == 'e':
                value += 5
            elif j == 4 and words_list[i][j] in ('e', 'y', 't', 'r', 'l', 'h', 'n', 'd'):
                value += 5
            elif j == 4 and words_list[i][j] == 's':
                value = 2
        if len(words_list[i]) != len(set(words_list[i])):
            value *= len(set(words_list[i])) / len(words_list[i])

        value = round(value, 2)
        values.append(value)
    words_list = np.array(words_list)
    values = np.array(values)
    indexes = values.argsort()
    words_list = words_list[indexes]
    return words_list


def main():
    file = open("D:\\Programming\\wordleSolver\\possible_words.txt")
    words = file.read()
    words = words.split('\n')
    words_final = []
    tmp = []
    for word in words:
        for char in word:
            tmp.append(char)
        words_final.append(tmp)
        tmp = []

    words = np.array(words_final)
    words = evaluation(words)

    print(len(words))
    words = words.tolist()

    words = misplaced_letters(['_', '_', '_', '_', 's'], words)
    words = misplaced_letters(['p', 'i', '_', '_', '_'], words)
    words = not_in_word_letters('tarehonymc', words)
    # words = correct_letters(['s', '_', '_', '_', '_'], words)
    # words = misplaced_letters(['_', 'l', '_', 'a', '_'], words)
    # words = misplaced_letters(['r', 'a', '_', '_', '_'], words)
    # words = misplaced_letters(['_', '_', '_', 'r', 'e'], words)
    # words = misplaced_letters(['_', '_', '_', 'e', 'r'], words)

    # words = misplaced_letters(['_', '_', '_', '_', 'e'], words)

    # # jak misplaced to nie mozna byc w miejscu w ktorym bylo
    print(len(words))
    writeToFile(words)

    # print(['_', '_', 'o', '_', '_'].filter(lambda val: val != '_'))


main()
