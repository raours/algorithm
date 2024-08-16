from collections import deque
import sys
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

N, K = map(int, input().split())
virus = []
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] !=0:
            virus.append([board[i][j],i,j,0])

S, X, Y = map(int, input().split())

virus.sort() #바이러스 번호순
q = deque(virus)

while q:
    v, x, y, s = q.popleft() #bfs: 1초마다 상하좌우로 뻗어나가므로
    if s == S:
        break
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<N: #범위안
            if board[nx][ny] ==0:#빈칸
                board[nx][ny] = v
                q.append([v, nx, ny, s+1])


print(board[X-1][Y-1])   

