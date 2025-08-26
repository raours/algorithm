'''
2025.8.26
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [1,0,-1,0,1,1,-1,-1]
dc = [0,1,0,-1,1,-1,1,-1]
def bfs(i,j):

    q = deque()
    q.append((i,j))
    board[i][j] = -1

    while q:
        curi,curj = q.popleft()

        for d in range(8):
            nr,nc = curi +dr[d], curj+dc[d]
            if 0<=nr<h and 0<=nc<w and board[nr][nc]==1:
                q.append((nr,nc))
                board[nr][nc] = -1 #방문처리


while True:
    w, h = map(int,input().split())
    if (w,h) == (0,0):
        break
    board = [list(map(int,input().split())) for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1: #land
                bfs(i,j)
                ans += 1


    print(ans)