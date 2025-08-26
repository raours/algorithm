'''
2025.8.26
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]
def bfs(i,j,er,ec):

    q = deque()
    q.append((i,j))
    board[i][j] = 1

    while q:
        curi,curj = q.popleft()
        if (curi,curj) == (er,ec):
            print(board[er][ec]-1)
            break

        for d in range(8):
            nr,nc = curi +dr[d], curj+dc[d]
            if 0<=nr<n and 0<=nc<n and board[nr][nc]== 0:
                q.append((nr,nc))
                board[nr][nc] = board[curi][curj]+1

T = int(input())
for _ in range(T):
    n = int(input()) #체스판 길이
    sr, sc = map(int,input().split())
    er, ec = map(int,input().split())

    board = [[0] * n for _ in range(n)]

    bfs(sr,sc,er,ec)