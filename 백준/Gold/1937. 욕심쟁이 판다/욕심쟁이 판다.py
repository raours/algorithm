'''
2025.8.7
백준 : 욕심쟁이 판다
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*n for _ in range(n)] #dp리스트 / 그 좌표에서 이동할 수 있는 값
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dfs(r,c):

    if dp[r][c] != -1: #이미 그 칸에서 이동할 수 있는 칸의 수 계산 되어 있을 때,
        return dp[r][c]

    dp[r][c] = 1

    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<n and board[nr][nc] > board[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr,nc)+1)

    return dp[r][c]

for i in range(n):
    for j in range(n):
        dfs(i,j)

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
print(ans)
