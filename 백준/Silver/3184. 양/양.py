'''
2025.8.30
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R,C = map(int,input().split())
lst = [list(input().strip()) for _ in range(R)]
dr = [0,-1,0,1]
dc = [-1,0,1,0]

def dfs(cr,cc):
    global sheep, wolf
    visit[cr][cc] = True
    if lst[cr][cc] == 'v': #늑대
        wolf += 1
    elif lst[cr][cc] == 'o': #양
        sheep += 1

    for k in range(4):
        nr, nc = cr+dr[k], cc+dc[k]
        if 0<=nr<R and 0<=nc<C and not visit[nr][nc] \
            and lst[nr][nc] != '#':
            dfs(nr,nc)
    return


total_sheep, total_wolf = 0,0
visit = [[False]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            sheep, wolf = 0,0
            dfs(i,j)
            if sheep> wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep,total_wolf)

