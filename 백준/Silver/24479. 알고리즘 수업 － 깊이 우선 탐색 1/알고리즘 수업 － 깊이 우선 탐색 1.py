'''
2025.8.28
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int,input().split())

lst = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    lst[u].append(v)
    lst[v].append(u)

for i in lst:
    i.sort()

def dfs(start):
    global cnt
    for next in lst[start]:
        if not visit[next]:
            cnt += 1
            visit[next] = cnt
            dfs(next)
    return



visit = [0] * (n + 1)
visit[r] = 1
cnt = 1
dfs(r)



for i in range(1,n+1):
    print(visit[i])

