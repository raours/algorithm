'''
2025.8.28
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int,input().split()) #문제에 가로가 n, 세로가 m이라고 되어있음
#문제를 항상 꼼꼼히 읽자!

dr = [0,1,-1,0]
dc = [1,0,0,-1]

lst = [list(map(str, input().strip())) for _ in range(n)]

def dfs(cr,cc):
    global cnt
    for k in range(4):
        nr, nc = cr+dr[k], cc+dc[k]
        if 0<=nr<n and 0<=nc<m and visit[nr][nc] == 0 \
            and lst[cr][cc] == lst[nr][nc]:
                cnt += 1
                visit[nr][nc] = 1
                dfs(nr,nc)

    return


our_sum = 0
they_sum = 0
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            cnt = 1
            visit[i][j] = 1
            dfs(i,j)
            if lst[i][j] == 'W':
                our_sum += (cnt*cnt)
            else:
                they_sum += (cnt*cnt)



print(our_sum, they_sum)


