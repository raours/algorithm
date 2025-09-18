'''
2025.9.18
'''
import sys
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    dp = [[0]*(n+1) for _ in range(k+1)]
    dp[0] = [0]+[i for i in range(1,n+1)] #0층!

    for i in range(1,k+1): #각 층마다
        for j in range(1,n+1): #각 호마다
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print(dp[k][n])
