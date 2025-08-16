'''
2025.8.15
'''
import sys

input = sys.stdin.readline

s = input().strip()

stack = []
flag = False
res = []
for i in range(len(s)):
    if s[i] == '<':
        if len(stack) >0 : #뒤집힌 글자 있으면
            res.extend(reversed(stack))
            stack = []

        flag = True
        res.append('<')
    elif s[i] == '>': #여기까지 tag
        flag = False
        res.append('>')

    elif s[i] == ' ':
        if flag:
            res.append(' ')
        else:
            res.extend(reversed(stack))
            stack = []
            res.append(' ')

    else: #문자 or 숫자
        if flag: #tag 안에 있으면,
            res.append(s[i]) #그냥 출력
        else : stack.append(s[i])

if len(stack) > 0:
    res.extend(reversed(stack))

print(''.join(res))