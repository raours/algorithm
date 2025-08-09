'''
2025.8.9
백준 : 합분해
'''
import sys

input = sys.stdin.readline

n, k = map(int,input().split())
dp = [[0] * (n+1) for _ in range(k+1)]

# dp 초기화
for i in range(n+1):
    dp[0][i] = 1
for j in range(k):
    dp[j][0] = 1

for i in range(1, k):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[k-1][n]%1000000000)
