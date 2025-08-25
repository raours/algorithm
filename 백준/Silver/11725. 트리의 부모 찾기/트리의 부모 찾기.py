'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

visit = [0] * (n+1)

q = deque()
q.append(1)
visit[1] = 1

while q:
    current = q.popleft()

    for next in tree[current]:
        if visit[next] == 0:
            q.append(next)
            visit[next] = current #뻗어나온 곳이 부모노드

print(*visit[2:], sep = '\n')