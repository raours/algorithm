'''
2025.8.9
백준 : 타일 채우기
'''
import sys

input = sys.stdin.readline
n = int(input())

if n % 2 != 0:
    print(0)
elif n == 2:
    print(3)
else:
    dp = [0] * (n+1)
    dp[2] = 3

    for i in range(4,n+1, 2):
        dp[i] = dp[i - 2] * 3 + 2 # 처음에 생각한 점화식
        # 이 부분이 추가되어야함! dp[2]~dp[n-4] 까지의 애들에 각각 *2(독보적인 문양!, n-2의 문양까지 나와있으니까)
        for j in range(2, i - 3, 2):
            dp[i] += (dp[j] * 2)

    print(dp[n])