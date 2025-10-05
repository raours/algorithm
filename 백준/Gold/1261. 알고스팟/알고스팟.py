'''
2025.10.5
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(r,c):
    q = deque()
    q.append((r,c,0)) #부순 벽 갯수
    visit = [[False]*(m) for _ in range(n)]
    visit[r][c] = True
    ans = -1
    while q:
        cr,cc,cnt = q.popleft()
        if (cr,cc) == (n-1,m-1):#도착
            ans = cnt

        for i in range(4):
            nr,nc = cr+dr[i], cc+dc[i]
            if 0<=nr<n and 0<=nc<m and visit[nr][nc] == False:
                if board[nr][nc] == 0: #빈 방이면, 우선적으로 돌도록 appendleft!!
                    q.appendleft((nr,nc,cnt))
                else:
                    q.append((nr,nc,cnt+1))
                visit[nr][nc] = True
    return ans


m,n = map(int,input().split())
board = []
for _ in range(n):
    temp = list(map(int,input().strip()))
    board.append(temp)

print(bfs(0,0))
