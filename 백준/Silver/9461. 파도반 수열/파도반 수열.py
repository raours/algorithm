'''
2025.9.20
'''
import sys
input=sys.stdin.readline

t = int(input())

dp = [0]*100
dp[0], dp[1], dp[2] = 1,1,1

for i in range(3,100): # 순서대로
    dp[i] = dp[i-3]+dp[i-2]

for _ in range(t):
    n = int(input())
    print(dp[n-1])