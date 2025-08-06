'''
2025.8.6
백준 : 내리막 길
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]
dp = [[-1] * m for _ in range(n)]

def dfs(r,c):
    # 종료 조건
    if (r,c) == (n-1,m-1): #맨 끝칸 도달했으면 return
        return 1

    if dp[r][c] != -1: #이미 r,c 점부터 도착점까지의 경우의 수를 구해놨다면 바로 반환
        return dp[r][c]

    dp[r][c] = 0 # (r,c) 점부터 도착점까지의 경우의 수를 이제부터 구하겠다!
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m and board[nr][nc] < board[r][c]:
            dp[r][c] += dfs(nr,nc) #그 다음 지점으로부터 거슬러 올라가 또 도착점 까지의 경우의 수를 구함
            #그걸 더해주며, 시작점까지 거슬러 올라오며 경우의 수를 갱신!

    return dp[r][c] #갱신한 경우의 수 반환!

print(dfs(0,0))
