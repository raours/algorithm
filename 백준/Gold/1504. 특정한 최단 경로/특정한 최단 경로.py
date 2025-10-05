'''
2025.10.5
'''
import sys
import heapq
input = sys.stdin.readline

INF = 1e9

def dijkstra(s):
    distance = [INF]*(n+1)
    hq = []
    heapq.heappush(hq,(0,s))
    distance[s] = 0 #시작점 거리 0으로 초기화

    while hq:
        dist,now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        for i in lst[now]:
            cost = dist+i[1]

            if cost<distance[i[0]]:
                heapq.heappush(hq,(cost,i[0]))
                distance[i[0]] = cost
    return distance


#1->v1, 1->v2 // v1->N, v2->N 이렇게 비교하면 되므로,
#간선의 가중치가 있는 최단경로 -> 다익스트라
n, e = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

v1, v2 = map(int, input().split())

temp = dijkstra(1)
temp_v1 = dijkstra(v1)
temp_v2 = dijkstra(v2)

ans = INF
#v1먼저갈때
ans = min(ans,temp[v1] + temp_v1[v2] + temp_v2[n])

#v2먼저갈때
ans = min(ans,temp[v2] + temp_v2[v1] + temp_v1[n])

if ans<INF: print(ans)
else: print(-1)