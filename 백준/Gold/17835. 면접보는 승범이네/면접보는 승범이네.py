import sys
import heapq

input = sys.stdin.readline


INF = int(1e11)
n, m, K = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v,c = map(int, input().split())
    graph[v].append((u,c)) #면접장 -> 도시로 다익스트라 하기 위해 반대로 저장

k = list(map(int, input().split())) # 면접장의 번호들
distance = [INF] * (n+1)

def dijstra():
    q = []
    for target in k:
        heapq.heappush(q, (0, target))  #모든 면접장에 대해 최단 거리 구하기
        distance[target] = 0

    while q:
        dis, now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]: #그 노드를 거쳐가는게 더 빠르면
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 모든 면접장에 대해 도시의 최단거리들을 구한 값은 
# -> 각각의 면접장에 대해 가장 가까운 면접장으로 가는 최단 거리를 구한 값이 됨
dijstra()

max_d = 0
max_index = 0
for index, d in enumerate(distance):
    if d != INF and d>max_d:
        max_d = d
        max_index = index

print(max_index)
print(max_d)