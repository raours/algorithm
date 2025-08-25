'''
2025.8.25
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    board = [[0]*m for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().split())
        board[x][y] = 1

    visit = [[0]*m for _ in range(n)]

    def bfs(i,j):
        q = deque()
        q.append((i,j))
        visit[i][j] = 1

        while q:
            x,y = q.popleft()

            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx = x+dx
                ny = y+dy

                if 0<= nx <n and 0<=ny<m and board[nx][ny] ==1 and visit[nx][ny] == 0:
                    q.append((nx,ny))
                    visit[nx][ny] = 1

        return


    ans = 0
    for i in range(n):
        for j in range(m): #모든 방문 안 한&배추 칸에 대해 bfs
            if board[i][j] == 1 and visit[i][j] == 0:
                bfs(i,j)
                ans += 1
    print(ans)