'''
2025.8.28
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

lst = []
dr = [0,1,-1,0]
dc = [1,0,0,-1]

for i in range(n):
    temp = list(map(str, input().strip()))
    lst.append(temp)
    for j in range(m):
        if temp[j] == 'I': #도연
            tr, tc = i, j
            lst[i][j] = 'X'

def dfs(cr,cc):
    global cnt
    for k in range(4):
        nr, nc = cr+dr[k], cc+dc[k]
        if 0<=nr<n and 0<=nc<m:
            if lst[nr][nc] == 'O': #빈공간
                lst[nr][nc] = 'X'
                dfs(nr,nc)

            elif lst[nr][nc] == 'P': #사람
                cnt += 1
                lst[nr][nc] = 'X'
                dfs(nr,nc)

    return


cnt = 0
dfs(tr,tc)

if cnt == 0:
    print("TT")
else:
    print(cnt)


