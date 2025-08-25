'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

connect = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    connect[x].append(y)
    connect[y].append(x)

q = deque()
q.append(1) #1번 컴퓨터 시작
visit = [0]*(n+1)
visit[1] = 1 #방문 처리
ans = 0

while q:
    current = q.popleft()
    for i in connect[current]: #이어져있는 곳 모두
        if visit[i] == 0: #방문한 적 없다면,
            q.append(i)
            ans += 1
            visit[i] = 1 #방문 처리

print(ans)