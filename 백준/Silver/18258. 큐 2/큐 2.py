'''
2025.8.17
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    s = input().strip()
    if s == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s == 'size':
        print(len(q))
    elif s == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(int(s[5:]))


