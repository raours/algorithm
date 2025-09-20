'''
2025.9.21
'''
import sys
input=sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0] + [1 for _ in range(9)]

for i in range(2,n+1):
    for j in range(10):
        #dp[i][j] : i길이, j로 끝나는 계단수 개수
        #i-1길이의 전의 수를 기준으로 구하면 됨!
        if j == 9: #그럼 전의 수는 무조건 8임
            dp[i][j] = dp[i-1][8]
        elif j == 0: #전의 수는 무조건 1
            dp[i][j] = dp[i - 1][1]
        else:
            dp[i][j] = dp[i - 1][j-1] + dp[i - 1][j+1]
print((sum(dp[n]))% 1000000000)