'''
2025.8.6
백준 : 동전1
'''
import sys

input = sys.stdin.readline

n,k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()

dp = [0] * (k+1) #k원 목표

#점화식 dp[i] = dp[i] + dp[i-coin]
#예시 : dp[3원] = dp[기존3원] + dp[3원 - coin(2원짜리 코인)]
#설명 : coin별로 하나씩 추가해서 쓰며 dp list 채우기
#예시는 2원짜리로 3원짜리를 만들려면 기존 3원을 만드는 방법에 + ( 1원 만들던 방법에 +2코인 더하면 3원 되니까 그 기존 1원 만들던 방법 더해줌)
dp[0] = 1 #초기값!
for c in coin:
    for i in range(c, k+1): #c원이면 c원부터 dp 리스트에 영향 주니까 c부터 시작!
        dp[i] = dp[i] + dp[i-c]

print(dp[k])

