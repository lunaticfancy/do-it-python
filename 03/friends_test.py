import os, re, codecs
# print(os.getcwd())
# with codecs.open(r'.\03\friends101.txt', 'r', encoding='utf-8') as f:
#     script101 = f.read()
#     # print(script101[:100])

#     Line = re.findall(r'Monica:.+', script101)
#     for i in Line[:3]:
#         print(i)

#     f1 = open(r'.\03\monica.txt', 'w', encoding='utf-8')
#     monica = ''
#     for i in Line:
#         monica += i

#     f1.write(monica)
#     f1.close

# with codecs.open(r'.\03\friends101.txt', 'r', encoding='utf-8') as f:
#     script101 = f.read()

#     # Line = re.findall(r'Monica:.+', script101)
#     # Character = re.findall(r'[A-Z].+:]', script101)
#     CharacterPattern = re.compile(r'[A-Z][a-z]+:')
#     Line = re.findall(CharacterPattern, script101)
#     Line = set(Line)
#     f1 = open(r'.\03\character.txt', 'w', encoding='utf-8')
#     characterList = ''
#     for i in Line:
#         characterList += i[:-1] + "\n"

    
#     f1.write(characterList)
#     f1.close

with codecs.open(r'.\03\friends101.txt', 'r', encoding='utf-8') as f:
    sentences = f.readlines()
    conversation = []
    for i in sentences:
        if (re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)):
            conversation.append(i)
    for i in conversation:
        print(i)
    with open(r'.\03\would.txt', 'w') as would:
        would.writelines(conversation)
    



