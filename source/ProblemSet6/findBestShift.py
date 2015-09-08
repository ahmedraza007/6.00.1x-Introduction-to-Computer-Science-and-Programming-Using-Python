from applyShift import applyShift
from parser import parser1
from ProblemSet6.ps6_encryption import isWord
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    max_best = 0
    best_shift = 0
    words = parser1(text)
    for i in range(26):
        validwords = 0
        for word in words:
            ret = applyShift(word, i)
            if isWord(wordList, ret):
                validwords += 1
                
            if validwords > max_best:
                max_best = validwords
                best_shift = i
                
    return best_shift

