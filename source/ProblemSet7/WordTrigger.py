import string
class WordTrigger(object):
    def __init__(self, word):
        self.word = word
        
    def isWordIn(self, text):
        for i in text:
            if i in string.punctuation:
                text = text.replace(i, " ")
        print text
        
        if " "+self.word+" " in text.lower():
            return True
        
        else:
            return False
                
test = WordTrigger("soft")
print test.isWordIn("Downey makes my clothes the softest they can be!")