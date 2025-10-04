'''
2025.10.4
'''
import sys
input = sys.stdin.readline

INF = 1e9
n,m = map(int,input().split())
lst = [[INF]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    lst[a-1][b-1] = 1

#플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

#lst[i][] 라인에 INF 보다 작은게 있으면 걔네는 i보다 큰 숫자들
#lst[][i] 라인에 INF보다 작으면, i보다 작은 숫자들
#그 개수들의 합이 n-1개면 ok!
cnt = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if lst[i][j] != INF:
            cnt[i].append(j)
            cnt[j].append(i)

ans = 0
for i in range(n):
    if len(cnt[i]) == n-1:
        ans += 1

print(ans)
