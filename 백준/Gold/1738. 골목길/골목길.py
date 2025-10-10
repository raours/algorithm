'''
2025.10.9
벨만포드, 역추적, bfs
'''
import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(n):
        updated = False #조기종료 조건
        for j in range(m):
            cur,nxt, cost = lst[j]

            if dist[cur] != -INF and dist[cur]+cost > dist[nxt]:
                dist[nxt] = dist[cur] + cost # 최대값으로 갱신
                prev[nxt] = cur #이전 노드 저장
                updated = True #갱신 됐음!

                if i == n-1: #n번째에서도 갱신된 노드 체크,
                    affected[cur] = True
                    affected[nxt] = True

        if not updated: #갱신된 노드가 없으면,
            break

    #n에 도달 가능한 정점 bfs로 한번에 찾기
    reach = [False] * (n+1)
    dq = deque()
    dq.append(n)
    reach[n] = True

    while dq:
        x = dq.popleft()

        for y in rg[x]:
            if not reach[y]:
                reach[y] = True
                dq.append(y)

    #reach & affected 겹치는 노드가 있으면, or 경로없으면 최대 경로x
    if any(affected[num] and reach[num] for num in range(1,n+1)) or dist[n] == -INF:
        print(-1)
        return

    #최대 경로가 있다면! 경로 역추적!
    path = []
    cur = n
    for _ in range(n):
        path.append(cur)
        if cur == 1: #도착점에 왔으면, 끝!
            break
        if prev[cur] != -1:
            cur = prev[cur]
        else: break

    print(*reversed(path))
    return


n,m = map(int,input().split())
lst = [] #모든 간선에 대한 정보
rg = [[] for _ in range(n+1)]  # 역그래프
for _ in range(m):
    u, v, w = map(int, input().split())
    lst.append((u,v,w))
    rg[v].append(u)
dist = [-INF] * (n+1)
prev = [-1] *(n+1)
affected = [False] * (n+1) #n번째 사이클에서 영향 받은 노드

bf(1)