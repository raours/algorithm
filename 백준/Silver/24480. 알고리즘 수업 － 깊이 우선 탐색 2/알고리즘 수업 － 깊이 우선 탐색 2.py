'''
2025.8.28
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int,input().split())
lst = [[] for _ in range(n+1)]

for i in range(m):
    x,y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

def dfs(cur):
    global cnt
    lst[cur].sort(reverse = True)
    for next in lst[cur]:
        if not visit[next]:
            cnt += 1
            visit[next] = cnt
            dfs(next)
    return

cnt = 1
visit = [0]*(n+1)
visit[r] = 1
dfs(r)


for k in range(1,n+1):
    print(visit[k])