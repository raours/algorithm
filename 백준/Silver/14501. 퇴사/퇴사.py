
N = int(input())
T = [0] * N
P = [0] * N
dp = [0] *(N+1)


for i in range(N):
    T[i], P[i] = map(int, input().split())

for n in range(N-1,-1,-1):
    if n+T[n] > N: #상담 x
        dp[n] = dp[n+1]
    else: 
        dp[n] = max(dp[n+1], P[n]+dp[n+T[n]])

print(dp[0])