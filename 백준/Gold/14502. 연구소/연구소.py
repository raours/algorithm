import sys
import itertools

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
lst = []
virus = []

for i in range(N): #1을 넣을 수 있는 자리
    for j in range(M):
        if board[i][j] == 0:
            lst.append((i,j))
        if board[i][j] == 2:
            virus.append((i,j))


combi = itertools.combinations(lst, 3)

def dfs(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if B[nx][ny] == 0:
                B[nx][ny] = 2
                dfs(nx, ny)
    
result = 0
for c in combi:
    B = [arr[:] for arr in board]
    for x, y in c:
        B[x][y] = 1 #벽세우기

    for i, j in virus: # 초기 virus 위치마다
        dfs(i,j)
    

    #안전영역 계산
    safe_area = sum(row.count(0) for row in B)
    result = max(result, safe_area)

print(result)
    