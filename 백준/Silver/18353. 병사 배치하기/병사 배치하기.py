import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.reverse()
dp = [1] * (N) #모두 기본 값은 길이 1임

#가장 긴 증가하는 부분 배열 점화식 쓰면 됨!
for i in range(N):
    for j in range(i):
        if lst[j] < lst[i]: #자기보다 작은 수들에게만 이어붙일 수 있음
            dp[i] = max(dp[i], dp[j]+1) #j<=i 구간에서 가장 긴 배열을 찾는 거기 때문에 max

print(N-max(dp))