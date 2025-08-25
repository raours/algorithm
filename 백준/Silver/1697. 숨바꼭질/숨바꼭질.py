'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visit = [0] * 100001

q = deque()
q.append(n)
visit[n] = 1

while q:
    current = q.popleft()
    if current == k:
        print(visit[current]-1)
        break
    for d in (-1, 1, current):
        next = current + d
        if 0<= next < 100001 and visit[next] == 0:
            q.append(next)
            visit[next] = visit[current]+1
