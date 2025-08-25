'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 1

    while q:
        current = q.popleft()

        for next in lst[current]:
            if visit[next] == 0:
                q.append(next)
                visit[next] = 1


visit = [0]*(n+1)
cnt = 0
for i in range(1,n+1):
    if visit[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)