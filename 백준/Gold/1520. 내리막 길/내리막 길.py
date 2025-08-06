import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

input = sys.stdin.readline

# 입력
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

# 방향: 동, 남, 서, 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# DP 배열: -1이면 아직 계산 안함, 0 이상이면 경로 수 저장
dp = [[-1] * n for _ in range(m)]

def dfs(r, c):
    # 도착 지점에 도달하면 경로 1개
    if r == m - 1 and c == n - 1:
        return 1

    # 이미 계산된 값이면 바로 반환
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0  # 초기화

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if board[nr][nc] < board[r][c]:  # 내리막길 조건
                dp[r][c] += dfs(nr, nc)

    return dp[r][c]

print(dfs(0, 0))
