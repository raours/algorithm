'''
2025.8.17
'''
import sys
from collections import deque
input = sys.stdin.readline

buffer = int(input())

q= deque()
while True:
    x = int(input())
    if x == -1:
        break

    if x == 0:
        q.popleft()
    elif x > 0 and len(q) < buffer:
        q.append(x)

print(*q)