import string
from buildcoder import buildCoder
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    result = ''
    for i in text:
        if i in string.punctuation or i == ' ' or i.isdigit():
            result += i
        
        else:
            result += coder[i]
    
    return result

# print applyCoder("Hello, world!", buildCoder(3))
# print applyCoder("Khoor, zruog!", buildCoder(23))
# print applyCoder("Ahmed Raza The great!!!", buildCoder(14))
# print applyCoder("Ovasr Fono Hvs ufsoh!!!", buildCoder(12))
        