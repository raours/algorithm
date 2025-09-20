'''
2025.9.20
'''
import sys
input=sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

if n == 1:
    print(lst[0])
elif n == 2:
    print(lst[0]+lst[1])
else:
    dp = [0] * 10001
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0]+lst[2], lst[1]+lst[2], dp[1])

    for i in range(3, n):
        # i-3번째까지의 최대값 + i-1,i번째 포도주
        # i-2번째까지의 최대값 + i번째 포도주 (i-1 x)
        # i번째 안 마심! : dp[i-1]
        dp[i] = max(dp[i-3]+lst[i-1] + lst[i], dp[i-2]+lst[i], dp[i-1])

    print(dp[n-1])
