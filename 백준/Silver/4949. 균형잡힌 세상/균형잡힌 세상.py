'''
2025.8.15
'''
import sys

input = sys.stdin.readline

letters = sys.stdin.readlines()
lst = []

sen = ''
for a in letters:
    lst.append(a.rstrip())
    
for j in range(len(lst)-1):
    l = lst[j]
    stack = []
    flag = True
    for i in range(len(l)):
        letter = l[i]
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')':
            if len(stack) == 0:
                flag = False
                break
            temp = stack.pop()
            if temp != '(':
                flag = False
                break

        elif letter == ']':
            if len(stack) == 0:
                flag = False
                break
            temp = stack.pop()
            if temp != '[':
                flag = False
                break

    if not flag or len(stack) > 0:
        print('no')
    else:
        print('yes')
