'''
2025.9.22
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
dp = [0]*(n+1)
lst = [[] for _ in range(n+1)]
con = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    lst[a].append(b)
    con[b] += 1
for j in range(1,n+1):
    if con[j] == 0:
        dp[j] = 1
    for i in lst[j]:
        dp[i] = max(dp[i], dp[j]+1)

for i in range(1,n+1):
    print(dp[i])

