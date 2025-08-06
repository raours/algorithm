'''
2025.8.6
백준 : 동전2
'''
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [100001] * (k+1) #min으로 계속 최소 동전 갯수로 갱신해야하므로 최대값으로 초기화
dp[0] = 0 #0을 만드는 동전 갯수는 0!
#점화식 dp[i] = min(dp[i], dp[i-coin]+1)
#직접 예시를 가지고 코인을 하나 추가할 때마다, 어떻게 최소값이 변하는지 확인하기
#설명: dp[i] 계속 갱신해나간다. = min(기존dp[i], dp[i-coin] 코인만큼 뺀 dp값에 +1(그 코인)을 더해준 갯수) 의 최솟값으로 갱신

for c in coin:
    for i in range(c,k+1):
        dp[i] = min(dp[i], dp[i-c]+1)

if 100001>dp[k]>0:
    print(dp[k])
else:
    print(-1)
