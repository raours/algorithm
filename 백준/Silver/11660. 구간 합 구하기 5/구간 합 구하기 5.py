'''
2025.9.5
'''
import sys

input=sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

sum_lst = [[0] * (n + 1) for _ in range(n+1)]

# 누적합 dp로 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_lst[i][j] = sum_lst[i][j-1] + sum_lst[i-1][j]+lst[i-1][j-1]-sum_lst[i-1][j-1]

for t in range(m):
    sr, sc, er, ec = map(int, input().split())
    ans = sum_lst[er][ec] - sum_lst[er][sc - 1] - sum_lst[sr - 1][ec] + sum_lst[sr - 1][sc - 1]
    print(ans)