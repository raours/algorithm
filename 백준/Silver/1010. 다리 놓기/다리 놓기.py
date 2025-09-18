'''
2025.9.18
'''
import sys
from itertools import combinations
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    dp = [[0]*(m+1) for _ in range(n)]
    dp[0] = [i for i in range(m+1)]

    for i in range(1,n):
        dp[i][i+1] = 1
        for j in range(i+2, m+1):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(dp[n-1][m])


