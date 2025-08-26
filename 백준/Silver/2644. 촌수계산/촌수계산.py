'''
2025.8.26
'''
import sys
from collections import deque
input = sys.stdin.readline

dr = [0,1,-1,0]
dc = [1,0,0,-1]
def bfs(t1,t2):

    q = deque()
    q.append((t1,0))
    visit = [0]*(n+1)
    visit[t1] = 1
    while q:
        curi, cnt = q.popleft()

        if curi == t2:
            return cnt

        for next in relation[curi]:
            if visit[next] == 0:
                q.append((next,cnt+1))
                visit[next] = 1

    return -1

n = int(input())
t1,t2 = map(int,input().split())
relation = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)


print(bfs(t1,t2))