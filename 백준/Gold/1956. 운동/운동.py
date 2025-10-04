'''
2025.10.4
'''
import sys
input = sys.stdin.readline

INF = 1e9
v,e = map(int,input().split())
lst = [[INF]*v for _ in range(v)]

for _ in range(e):
    a,b,c = map(int,input().split())
    lst[a-1][b-1] = c

#플로이드 워셜
for k in range(v):
    for i in range(v):
        for j in range(v):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])


ans = INF
for i in range(v):
    if lst[i][i] != INF: #사이클이 있으면,
        ans = min(ans, lst[i][i])

if ans == INF:
    print(-1)
else: print(ans)



