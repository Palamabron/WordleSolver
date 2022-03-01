import PySimpleGUI as sg
import level1
import level2
import freqFilter


# import tinker
# def calculate():
#     first_word = "tares"
def wordToStateList(word, result):
    misplaced = []
    correct = []
    wrongs = ""
    for i in range(len(result)):
        if result[i] == 'c':
            correct.append(word[i])
        else:
            correct.append('_')

    for i in range(len(result)):
        if result[i] == 'm':
            misplaced.append(word[i])
        else:
            misplaced.append('_')

    for i in range(len(result)):
        if result[i] == 'w':
            wrongs += word[i]

    return correct, misplaced, wrongs


def getLetter(isDisabled, identity):
    return sg.InputText(size=2, disabled=isDisabled, key=identity, enable_events=True)


def allWordsToList():
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
    return words_final


def getBestWord(words, possible_words):
    bitsValues = level2.evaluate(words, possible_words)
    words, bitsValues = level2.sort(bitsValues, possible_words)
    return words[-1]


def filterWordsList(words, correct, misplaced, wrong):
    if correct != ['_'] * 5:
        words = level1.correct_letters(correct, words)
    if misplaced != ['_'] * 5:
        words = level1.misplaced_letters(misplaced, words)
    if len(wrong) > 0:
        words = level1.not_in_word_letters(wrong, words)
    return words

# nie znalazło 'novel'
def createGUI():
    result_list = allWordsToList()
    possible_words = allWordsToList()
    sg.theme('DarkBlack1')
    isFirstOn = False
    isOtherOn = True
    bestWord = None

    keys = [['w10', 'w11', 'w12', 'w13', 'w14'], ['w20', 'w21', 'w22', 'w23', 'w24'],
            ['w30', 'w31', 'w32', 'w33', 'w34'], ['w40', 'w41', 'w42', 'w43', 'w44'],
            ['w50', 'w51', 'w52', 'w53', 'w54'], ['w60', 'w61', 'w62', 'w63', 'w64']]

    row = 0

    column = [
        [sg.Text('Enter c if correct, m if misplaced, w if wrong')],
        [sg.Text('Best word: TARES \tcomb: ' + str(len(result_list)), key='r1')],
        [getLetter(isFirstOn, 'w10'), getLetter(isFirstOn, 'w11'), getLetter(isFirstOn, 'w12'),
         getLetter(isFirstOn, 'w13'),
         getLetter(isFirstOn, 'w14'),
         sg.Button('Enter', key='w1'), sg.Text('Progress: ', key='p1')],
        [sg.Text('Best word:', key='r2')],
        [getLetter(isOtherOn, 'w20'), getLetter(isOtherOn, 'w21'), getLetter(isOtherOn, 'w22'),
         getLetter(isOtherOn, 'w23'),
         getLetter(isOtherOn, 'w24'),
         sg.Button('Enter', key='w2', disabled=True)],
        [sg.Text('Best word: ', key='r3')],
        [getLetter(isOtherOn, 'w30'), getLetter(isOtherOn, 'w31'), getLetter(isOtherOn, 'w32'),
         getLetter(isOtherOn, 'w33'),
         getLetter(isOtherOn, 'w34'),
         sg.Button('Enter', key='w3', disabled=True)],
        [sg.Text('Best word: ', key='r4')],
        [getLetter(isOtherOn, 'w40'), getLetter(isOtherOn, 'w41'), getLetter(isOtherOn, 'w42'),
         getLetter(isOtherOn, 'w43'),
         getLetter(isOtherOn, 'w44'),
         sg.Button('Enter', key='w4', disabled=True)],
        [sg.Text('Best word: ', key='r5')],
        [getLetter(isOtherOn, 'w50'), getLetter(isOtherOn, 'w51'), getLetter(isOtherOn, 'w52'),
         getLetter(isOtherOn, 'w53'),
         getLetter(isOtherOn, 'w54'),
         sg.Button('Enter', key='w5', disabled=True)],
        [sg.Text('Best word: ', key='r6')],
        [getLetter(isOtherOn, 'w60'), getLetter(isOtherOn, 'w61'), getLetter(isOtherOn, 'w62'),
         getLetter(isOtherOn, 'w63'),
         getLetter(isOtherOn, 'w64'),
         sg.Button('Enter', key='w6', disabled=True)],
        [sg.Button('Exit')]]
    # layout = [sg.Output(size=(12, 12)), sg.Column(column)]
    window = sg.Window('WordleSolver', column)
    # wrong -> w        misplaced -> m         correct -> c
    while True:  # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        for key in keys[row]:
            if not (values[key] == 'w' or values[key] == 'm' or values[key] == 'c'):
                window.Element(key).Update('')

        isFilled = True
        for key in keys[row]:
            if len(values[key]) != 1:
                isFilled = False
                break

        if event == 'w1' and isFilled:
            window['w10'].update(disabled=True)
            window['w11'].update(disabled=True)
            window['w12'].update(disabled=True)
            window['w13'].update(disabled=True)
            window['w14'].update(disabled=True)
            window['w20'].update(disabled=False)
            window['w21'].update(disabled=False)
            window['w22'].update(disabled=False)
            window['w23'].update(disabled=False)
            window['w24'].update(disabled=False)
            window['w1'].update(disabled=True)
            window['w2'].update(disabled=False)
            window['p1'].update('Progress: 0%')
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList('tares', states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            print(len(result_list))
            # zrobić top 3
            tmp = []
            isGood = True
            for el in possible_words:
                if len(set(el)) == 5:
                    for letter in ('q', 'x', 'j', 'z', 'v', 'w', 'f', 'k', 'g', 'b'):
                        if letter in el:
                            isGood = False
                            break
                    if isGood:
                        tmp.append(el)
                    else:
                        isGood = True

            tmp.remove(['t', 'a', 'r', 'e', 's'])
            bestWord = getBestWord(result_list, tmp)
            bestWord = bestWord.tolist()
            bestWord = "".join(bestWord)
            window['r2'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
            row += 1
        elif event == 'w2' and isFilled:
            window['w20'].update(disabled=True)
            window['w21'].update(disabled=True)
            window['w22'].update(disabled=True)
            window['w23'].update(disabled=True)
            window['w24'].update(disabled=True)
            window['w30'].update(disabled=False)
            window['w31'].update(disabled=False)
            window['w32'].update(disabled=False)
            window['w33'].update(disabled=False)
            window['w34'].update(disabled=False)
            window['w2'].update(disabled=True)
            window['w3'].update(disabled=False)
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList(bestWord, states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            print(len(result_list))
            if len(result_list) > 50:
                bestWord = getBestWord(result_list, possible_words)
                bestWord = "".join(bestWord)
            else:
                bestWord = freqFilter.getCommonWord(result_list)
                bestWord = "".join(bestWord)
            window['r3'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
            row += 1
        elif event == 'w3' and isFilled:
            window['w30'].update(disabled=True)
            window['w31'].update(disabled=True)
            window['w32'].update(disabled=True)
            window['w33'].update(disabled=True)
            window['w34'].update(disabled=True)
            window['w40'].update(disabled=False)
            window['w41'].update(disabled=False)
            window['w42'].update(disabled=False)
            window['w43'].update(disabled=False)
            window['w44'].update(disabled=False)
            window['w3'].update(disabled=True)
            window['w4'].update(disabled=False)
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList(bestWord, states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            bestWord = freqFilter.getCommonWord(result_list)
            bestWord = "".join(bestWord)
            window['r4'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
            row += 1
        elif event == 'w4' and isFilled:
            window['w40'].update(disabled=True)
            window['w41'].update(disabled=True)
            window['w42'].update(disabled=True)
            window['w43'].update(disabled=True)
            window['w44'].update(disabled=True)
            window['w50'].update(disabled=False)
            window['w51'].update(disabled=False)
            window['w52'].update(disabled=False)
            window['w53'].update(disabled=False)
            window['w54'].update(disabled=False)
            window['w4'].update(disabled=True)
            window['w5'].update(disabled=False)
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList(bestWord, states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            bestWord = result_list[0]
            bestWord = "".join(bestWord)
            window['r5'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
            row += 1
        elif event == 'w5' and isFilled:
            window['w50'].update(disabled=True)
            window['w51'].update(disabled=True)
            window['w52'].update(disabled=True)
            window['w53'].update(disabled=True)
            window['w54'].update(disabled=True)
            window['w60'].update(disabled=False)
            window['w61'].update(disabled=False)
            window['w62'].update(disabled=False)
            window['w63'].update(disabled=False)
            window['w64'].update(disabled=False)
            window['w5'].update(disabled=True)
            window['w6'].update(disabled=False)
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList(bestWord, states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            bestWord = result_list[0]
            bestWord = "".join(bestWord)
            window['r5'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
            row += 1
        elif event == 'w6' and isFilled:
            window['w60'].update(disabled=True)
            window['w61'].update(disabled=True)
            window['w62'].update(disabled=True)
            window['w63'].update(disabled=True)
            window['w64'].update(disabled=True)
            window['w6'].update(disabled=True)
            states = ''
            for key in keys[row]:
                states += values[key]
            correct_list, misplaced_list, wrongs = wordToStateList(bestWord, states)
            result_list = filterWordsList(result_list, correct_list, misplaced_list, wrongs)
            bestWord = result_list[0]
            bestWord = "".join(bestWord)
            window['r6'].update('Best word is: ' + str(bestWord).upper() + "\tcomb: " + str(len(result_list)))
    window.close()


createGUI()
