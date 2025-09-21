'''
2025.9.22
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
for idx in range(1, n+1):
    t,k,*tmp = map(int,input().split()) #unpacking사용
    dp[idx] = t

    for j in tmp: #선행작업이 있으면,
        dp[idx] = max(dp[idx], dp[j]+t)

print(max(dp))