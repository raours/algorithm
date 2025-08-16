'''
2025.8.15
'''
import sys

input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    s = input().strip()

    if s == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif s == '3':
        print(len(stack))
    elif s == '4':
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif s == '5':
        if len(stack)>0:
            print(stack[-1])
        else: print(-1)
    else:
        x = int(s[2:])
        stack.append(x)


