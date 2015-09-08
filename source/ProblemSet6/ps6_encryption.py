# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()

def getStorydecrypt():
    """
    Returns a story in decrypted texr
    """
    return open("story2.txt", "r").read()

# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def string_todict(lc, shift):
    """
    returns a circular string of characters converted to dicts with a certian shift
    provided as the input
    
    shift: 0 <= int < 26
    returns: dict
    """
    d = dict()
    for i in range(len(lc)):
        try:
            d[lc[i]] = lc[i+shift]
        except IndexError:
            if (i + shift) >= 25:
                j = (i + shift) - 25
                d[lc[i]] = lc[j - 1]
            continue
    return d


def mergedicts(d, f):
    """
    merges two dictionaries to give output as one dict
    """
    return dict(d.items() + f.items())


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.
  
    shift: 0 <= int < 26
    returns: dict
    """
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    d = string_todict(lc, shift)
    f = string_todict(uc, shift)
    q = mergedicts(d,f)
    return q

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = ''
    for i in text:
        if i in string.punctuation or i == ' ' or i.isdigit() or i == '\n':
            result += i
        
        else:
            result += coder[i]
    
    return result

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    coder = buildCoder(shift)
    return applyCoder(text, coder)
#
# Problem 2: Decryption
#

def parser1(text):
    count = 0
    word = ''
    z = []
    words = text.split(" ")
    
    for word in words:
        for i in word:
            if i in string.punctuation or i == ' ' or i.isdigit():
                z.append(word.replace(i, ""))
    if z == []:
        return words
    else:
        return z


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


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    wordList = loadWords()
    r = findBestShift(wordList, text)
    return applyShift(text, r)

def encryptStory(key):
    """
    to encrypt the story, according to our key.
    
    key: is the key value for encryption
    """
    text = getStorydecrypt()
    return applyShift(text, key)
    

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
#     wordList = loadWords()
#     s = applyShift('Hello, world!', 8)
#     bestShift = findBestShift(wordList, s)
#     assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    text = decryptStory()
    print text
    print encryptStory(8)