'''
2025.10.4
'''
import sys
input = sys.stdin.readline

INF = 1e9
n = int(input().strip())
m = int(input().strip())

lst = [[INF]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    lst[b - 1][a - 1] = 1

#플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

for i in range(n):
    temp = 0
    for j in range(n):
        if lst[i][j] < INF or lst[j][i] < INF:
            temp += 1
    print(n-1-temp)



