'''
2025.10.4
'''
import sys
input = sys.stdin.readline

INF = 1e9
n = int(input().strip())

lst = [[INF]*n for _ in range(n)]
while True:
    a, b = map(int, input().split())
    if (a,b) == (-1,-1):
        break
    lst[a - 1][b - 1] = 1
    lst[b - 1][a - 1] = 1

for i in range(n):
    lst[i][i] = 0 #사이클이 있으므로, 자기자신 정점 0으로 두기!

#플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

ans = INF
num = []
for i in range(n):
    if max(lst[i]) < ans:
        ans = max(lst[i])

for i in range(n):
    if max(lst[i]) == ans:
        num.append(i+1)

print(ans, len(num))
print(*num)



