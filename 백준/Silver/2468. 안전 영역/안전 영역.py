'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

mx = 0
mn = 101
for i in range(n):
    mx = max(mx, max(board[i]))
    mn = min(mn, min(board[i]))

def bfs(i,j,rain):

    q = deque()
    q.append((i,j))
    visit[i][j] = 1

    while q:
        curi,curj = q.popleft()

        for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr,nc = curi +dr, curj+dc
            if 0<=nr<n and 0<=nc<n and board[nr][nc]>rain and visit[nr][nc] == 0:
                q.append((nr,nc))
                visit[nr][nc] = 1


ans = 1
for rain in range(mn, mx):
    #모든 비에 대해

    area = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and board[i][j] > rain:
                bfs(i,j,rain)
                area += 1

    ans = max(ans, area)
print(ans)