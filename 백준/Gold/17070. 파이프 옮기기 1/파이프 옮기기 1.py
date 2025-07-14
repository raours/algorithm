'''
2025.7.14
백준 : 파이프옮기기1
'''
import sys

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1 #(r,c)오른쪽 좌표, 놓여진 방향 -> 그 상태에 도달할 수 있는 경우의 수


for nr in range(n):
    for nc in range(2,n):
        if lst[nr][nc] ==1: #벽이면, pass
            continue
        #가로가 되려면, 그전에는 가로 or 대각선
        dp[nr][nc][0] = dp[nr][nc-1][0] + dp[nr][nc-1][2]

        #세로가 되려면, 그전엔 세로 or 대각선 
        dp[nr][nc][1] = dp[nr-1][nc][1] + dp[nr-1][nc][2]


        #대각선이 되려면, 그전엔 가로 or 세로 or 대각선 
        if lst[nr-1][nc] == 0 and lst[nr][nc-1] ==0: #대각선이 될려면 위옆 추가로 비어있어야함
            dp[nr][nc][2] = dp[nr-1][nc-1][0] + dp[nr-1][nc-1][1] + dp[nr-1][nc-1][2]

print(dp[n-1][n-1][0]+dp[n-1][n-1][1]+dp[n-1][n-1][2])
                

