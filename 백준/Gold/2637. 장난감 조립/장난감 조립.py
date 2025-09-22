'''
2025.9.22
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
cnt = [0]*(n+1)
cnt[n] = 1 #완제품이 기준점
indegree = [0] * (n+1)

for _ in range(m):
    x,y,k = map(int,input().split())
    lst[x].append((y,k))
    indegree[y] += 1 #진입차수 +1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()

    for nxt, c in lst[cur]:
        cnt[nxt] += cnt[cur]*c
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1,n+1):
    if len(lst[i]) == 0:
        print(i, cnt[i])

