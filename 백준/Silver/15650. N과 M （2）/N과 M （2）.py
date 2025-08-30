'''
2025.8.30
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

def dfs(num, temp):
    if len(temp) == m:
        ans.add(temp)
        return

    for j in range(num+1, n+1):
        visit[j] = True
        dfs(j, temp+str(j))

ans = set()
visit = [False] * (n+1)
for i in range(1,n-m+2):
    visit[i] = True
    dfs(i,str(i))

ans = sorted(ans)
for s in ans:
    print(' '.join(s))

