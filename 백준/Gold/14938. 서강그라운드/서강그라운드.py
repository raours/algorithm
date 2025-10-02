'''
2025.10.2
'''
import sys
input = sys.stdin.readline

INF = 1e9
n,m,r = map(int,input().split())
items = list(map(int,input().split()))
lst = [[INF]*n for _ in range(n)]

for _ in range(r):
    a,b,l = map(int,input().split())
    lst[a-1][b-1] = l
    lst[b-1][a-1] = l

#플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

ans = 0
#어떤 지역에서 최대로 얻게 될지 모르니까 다 해보기
for i in range(n):
    temp = 0
    for j in range(n):
        if i == j: #자기 지역이면 획득
            temp += items[i]
        elif lst[i][j] <= m: #수색범위 안이면, 획득
            temp += items[j]
    ans = max(ans, temp)
print(ans)