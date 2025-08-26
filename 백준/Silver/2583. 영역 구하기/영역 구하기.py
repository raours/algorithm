'''
2025.8.26
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [0,1,-1,0]
dc = [1,0,0,-1]
def bfs(i,j):

    q = deque()
    q.append((i,j))
    board[i][j] = 1
    temp = 1
    while q:
        curi,curj = q.popleft()

        for d in range(4):
            nr,nc = curi +dr[d], curj+dc[d]
            if 0<=nr<n and 0<=nc<m and board[nr][nc]== 0:
                q.append((nr,nc))
                board[nr][nc] = 1
                temp += 1

    return temp

m,n,k = map(int,input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    x1,y1, x2, y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1 #좌표에 직사각형 표시


ans = []
cnt = 0
#각 영역 구하기
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans.append(bfs(i,j))
            cnt += 1
ans.sort()
print(cnt)
print(*ans)