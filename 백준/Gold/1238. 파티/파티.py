'''
2025.10.5
'''
import sys
import heapq
input = sys.stdin.readline

INF = 1e9

def dijkstra(s):
    global x_lst
    distance = [INF]*(n+1)
    hq = []
    heapq.heappush(hq, (0,s))
    distance[s] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if dist>distance[now]: #최단경로x
            continue

        for i in lst[now]: #갈 수 있는 다음 노드에 대해,
            cost = dist+i[1]

            if cost < distance[i[0]]: #최단경로면
                heapq.heappush(hq, (cost, i[0]))
                distance[i[0]] = cost #최단경로로 갱신

    if s == x: #목적지에 대한 다익이었으면,
        x_lst = distance[:]
    else:
        go_lst[s] = distance[x]

n,m,x = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b,c))

x_lst = []
go_lst = [0]*(n+1)
for i in range(1,n+1): #1~n 학생에 대해 각각 다익스트라
    dijkstra(i)

ans = 0
for i in range(1,n+1):
    if i == x:
        continue
    if ans<go_lst[i]+x_lst[i]:
        ans = go_lst[i]+x_lst[i]

print(ans)