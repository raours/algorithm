'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0]* m for _ in range(n)]

for i in range(n):
    temp = list(input().strip())
    for j in range(m):
        if int(temp[j]) == 1:
            board[i][j] = 1

q = deque()
q.append((0,0,0))
board[0][0] = -1 # 방문표시

while q:
    r,c,dis = q.popleft()
    if (r,c) == (n-1,m-1): #도착
        print(dis+1)
        break
    for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
        nr,nc = r+dr, c+dc

        if 0<=nr<n and 0<=nc<m and board[nr][nc] == 1:
            q.append((nr,nc,dis+1))
            board[nr][nc] = -1