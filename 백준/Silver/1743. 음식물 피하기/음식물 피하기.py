'''
2025.8.28
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int,input().split())
lst = [[0]*m for _ in range(n)]
dr = [0,1,-1,0]
dc = [1,0,0,-1]

for i in range(k):
    x,y = map(int, input().split())
    lst[x-1][y-1] = 1

def dfs(cr,cc):
    global cnt
    for d in range(4):
        nr, nc = cr + dr[d], cc + dc[d]
        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 1:
            lst[nr][nc] = -1
            cnt += 1
            dfs(nr,nc)
    return




ans = 0
for i in range(n):
    for j in range(m):

        if lst[i][j] == 1:
            lst[i][j] = -1 #방문 처리
            cnt = 1
            dfs(i,j)

            ans = max(ans, cnt)
print(ans)