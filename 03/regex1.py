import re
example = '이동민 교수님은 다음과 같이 설명했습니다.(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다.(최재영, 2019). 또 다른 견해도 있었습니다.(Lion, 2018)'
result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
# print(result)


def refinder(pattern, script):
    if re.match(pattern, script):
        print("Match!!!")
    else:
        print("Not Match!!!")


pattern = r'is'
script = 'Life is so cool'
# refinder(pattern, script)

# print(re.search('is', script))

number = 'My number is 511223-1******* and your is 521012-2*******'
# print(re.findall('\d{6}', number))

example1 = '저는 87년에 태어났습니다. 97년에는 IMF가 있년습니다. 지금은 2022년 입니다.'
result = re.findall(r'\d.+년', example1)
# . (greed)탐욕스럽다. 숫자가 나오고 어떠한 글자가 오든지 반복하고 년으로 끝나는 문장을 리턴 한다.
print(result)

result = re.findall(r'\d.+?년', example1)
# 숫자가 나오고 숫자가 반복되고 년으로 끝나면 한 패턴으로 인식 한다.
print(result)

result = re.findall(r'\d+.년', example1)
# 숫자가 나오고 숫자가 반복되고 년으로 끝나면 한 패턴으로 인식 한다.
print(result)


# split & [] (or)
sentence = 'I love a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
result = re.split(r'[.!?]', sentence)
print(result)


data = 'a:1; b:2; c:3'
for i in re.split(r';', data):
    i = i.removeprefix(' ')
    print(re.split(r':', i))


result = re.sub(r'dog', 'cat', sentence)
print(result)


words = 'I am home now. \n\n\nI am with my cat.\n\n'
print(words)
print(re.sub(r'\n', '', words))

result = re.findall(r'\w+ly', sentence)
print(result)

