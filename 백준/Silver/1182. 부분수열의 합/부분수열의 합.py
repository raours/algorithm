'''
2025.8.30
'''
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,total = map(int,input().split())
lst = list(map(int,input().split()))


s = []
visit = [False]*n
ans = 0
def dfs():
    global ans
    if len(s)>0 and sum(s) == total:
        ans += 1

    for i in range(n):
        if visit[i]:
            return
        s.append(lst[i])
        visit[i] = True
        dfs()
        s.pop()
        visit[i] = False

dfs()
print(ans)