'''
2025.10.14
'''

import sys
from collections import deque
# 1. 입력 받기
input = sys.stdin.readline
INF = -1e9
n,s,e,m = map(int,input().split())
lines = []
route = [[] for _ in range(n)]
for i in range(m):
    x,y,c = map(int,input().split())
    lines.append((x,y,c))
    route[y].append(x) #역
get_lst = list(map(int,input().split()) )
d = [INF] * n
visit = [False]*n

def solve():
    #끝
    q = deque()
    q.append(e)
    chk = [False] * n
    chk[e] = True

    while q:
        cur = q.popleft()
        for nxt in route[cur]:
            if not chk[nxt]:
                q.append(nxt)
                chk[nxt] = True

    if not chk[s]:
        print('gg')
        return

    d[s] = get_lst[s] #시작점은 갱신!
    #2.로직
    for i in range(n):
        for j in range(m):
            start, end, cost = lines[j]

            if d[start] != INF and d[start]-cost+get_lst[end] > d[end]:
                d[end] = d[start]-cost+get_lst[end]

                if i == n-1:
                    visit[start] = True
                    visit[end] = True

    if any(visit[i] and chk[i] for i in range(n)):
        print('Gee')
        return

    print(d[e])
    return



solve()