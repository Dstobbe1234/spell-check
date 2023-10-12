# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    exit = False
    while not exit:
        print('Main Menu')
        print('1: Spell Check a Word (Linear Search)')
        print('2: Spell Check a Word (Binary Search)')
        print('3: Spell Check Alice In Wonderland (Linear Search)')
        print('4: Spell Check Alice In Wonderland (Binary Search)')
        print('5: Exit')
        choice = int(input('Select an option '))
        if(choice == 1):
            spellCheckWord(linearSearch, dictionary)
        elif(choice == 2):
            spellCheckWord(binarySearch, dictionary)
        elif(choice == 3):
            spellCheckAlice(linearSearch, dictionary, aliceWords)
        elif(choice == 4):
            spellCheckAlice(binarySearch, dictionary, aliceWords)
        else:
            exit = True



def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()




def spellCheckWord(alg, array):
    word = input('enter word: ')
    time1 = time.time()
    response = alg(array, word)
    time2 = time.time()
    if(response > -1):
        print(f'{word} found in dictionary at position {response}. Time = {time2 - time1} seconds')
    else:
        print(f'{word} not found in dictionary. Time = {time2 - time1} seconds')
    
def spellCheckAlice(alg, array, text):
    time1 = time.time()
    totWords = 0
    for word in text:
        word = word.lower()
        if(alg(array, word) == -1):
                totWords+=1
        time2 = time.time()
    print(f'total words not found in dictionary: {totWords}. Time = {time2 - time1} seconds')

def linearSearch(array, item):
    for i in range(len(array)):
        if(array[i] == item):
            return i
    return -1

def binarySearch(array, item):
    LI = 0
    UI = len(array) -1
    while(LI <= UI):
        MI = (UI + LI) // 2
        if item == array[MI]:
            return MI
        elif item < array[MI]:
            UI = MI - 1
        else:
            LI = MI + 1
    return -1


main()