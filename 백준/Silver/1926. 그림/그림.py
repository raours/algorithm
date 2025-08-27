import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# cnt, wide
def dfs(r, c):
    global wide
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == 0 and board[nr][nc] == 1:
            visit[nr][nc] = visit[r][c] + 1
            wide += 1
            dfs(nr, nc)
    return

cnt, ans = 0, 0
visit = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            wide = 1
            dfs(i, j)
            cnt += 1
            ans = max(ans, wide)

print(cnt)
print(ans)