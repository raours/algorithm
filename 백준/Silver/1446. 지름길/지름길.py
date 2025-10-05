'''
2025.10.5
'''
import sys
import heapq
input = sys.stdin.readline

INF = 1e9

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]: #지금 hq에서 뺀 것이 최소경로가 아니라면
            continue #pass

        for i in lst[now]: #그 다음 연결되어 있는 노드로의 계산
            cost = dist+i[1] #다음노드까지의 거리가,

            if cost<distance[i[0]]: #더 최소 경로라면,
                distance[i[0]] = cost #갱신
                heapq.heappush(hq, (cost, i[0])) #최소경로인 다음노드와 그떄까지의 거리 hq에 push



n,d = map(int, input().split())

lst = [[] for _ in range(d+1)] #고속도로의 한 거리거리를 하나의 노드로 봄
distance = [INF] *(d+1) #각 노드에 대한 거리 초기화

#지름길 없는 일반 고속도로들은 i->i+1 까지 이동거리 1
#갈 수 있는 길에 대한 정보 입력
for i in range(d):
    lst[i].append((i+1,1))

#지름길에 대한 정보 업데이트!
for _ in range(n):
    a, b, c = map(int, input().split())
    if b>d: #벗어난 지름길은 pass
        continue
    lst[a].append((b,c))

#이 루트들 정보를 가지고 다익스트라!
dijkstra(0) #시작점은 0km 지점
print(distance[d])

