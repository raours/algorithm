'''
2025.8.15
'''
import sys

input = sys.stdin.readline

s = input().strip()

stack = []
flag = False
for i in range(len(s)):
    if s[i] == '<':
        if len(stack) >0 : #뒤집힌 글자 있으면
            stack.reverse()
            print(*stack, sep = '', end= '')
            stack = []

        flag = True
        print('<', end = '')
    elif s[i] == '>': #여기까지 tag
        flag = False
        print('>', end = '')

    elif s[i] == ' ':
        stack.reverse()
        print(*stack, sep='', end=' ')
        stack = []

    else: #문자 or 숫자
        if flag: #tag 안에 있으면,
            print(s[i], end='') #그냥 출력
        else : stack.append(s[i])

if len(stack) > 0:
    stack.reverse()
    print(*stack, sep='', end='')