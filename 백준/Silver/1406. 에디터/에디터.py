'''
2025.8.15
'''
import sys

input = sys.stdin.readline

left = list(input().strip())
right = []
n = int(input())

for _ in range(n):
    s = input().strip()

    if s == 'B':
        if len(left)>0:
            left.pop()
    elif s == 'L':
        if len(left) > 0:
            x = left.pop()
            right.append(x)
    elif s == 'D':
        if len(right) > 0:
            x = right.pop()
            left.append(x)
    else:
        left.append(s[2])
print(*left, sep = '', end = '')
right.reverse()
print(*right, sep = '')