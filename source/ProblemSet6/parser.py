import string
def parser1(text):
    count = 0
    word = ''
    z = []
    words = text.split(" ")
    
    for word in words:
        for i in word:
            if i in string.punctuation or i == ' ' or i.isdigit():
                z.append(word.replace(i, ""))
    
    return z
        
#         else:
#             result += coder[i]
#             
#     for i in range(len(text)):
#         if text[i] in string.punctuation or text[i] == ' ' or text[i].isdigit():
#         
#         else:
#             word += text[i]
#             continue
#     return z
print parser1("Hello, World!")