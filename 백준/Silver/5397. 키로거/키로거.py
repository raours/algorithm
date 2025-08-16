'''
2025.8.16
'''
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    left = []
    right = []
    for i in range(len(s)):
        if s[i] == '<':
            if len(left) > 0:
                right.append(left.pop())
        elif s[i] == '>':
            if len(right) > 0:
                left.append(right.pop())
        elif s[i] == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(s[i])

    left.extend(reversed(right))
    print(*left, sep = '')