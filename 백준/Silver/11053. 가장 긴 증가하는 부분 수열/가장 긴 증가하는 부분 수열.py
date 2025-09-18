'''
2025.9.18
'''
import sys
input=sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1]*n

for i in range(1,n): # 순서대로
    for j in range(i): # 그 앞의 숫자들보다 큰 숫자인 경우
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1) #전 숫자의 길이 +1 중에 큰 걸로
print(max(dp))