'''
2025.10.6
가중치 있는 최단 경로 ->다익스트라
경로추적 -> 역추적
'''
import sys
import heapq
input = sys.stdin.readline

INF = 1e9
def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0
    back_lst[s-1] = s-1

    while hq:
        cost,now = heapq.heappop(hq)
        if cost > distance[now]: # 우선순위!
            continue
        for i in route[now]: #다음으로 갈 수 있는 노드에 대해 최단거리 확인
            if cost+i[1] < distance[i[0]]:
                distance[i[0]] = cost+i[1]
                heapq.heappush(hq, (distance[i[0]],i[0]))
                back_lst[i[0]] = now

#입력
n = int(input().strip())
m = int(input().strip())
route = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    route[a-1].append((b-1,c))
distance = [INF] * n
s, e = map(int,input().split())

back_lst = [-1]*n #이전 지점 저장할 리스트
dijkstra(s-1)

print(distance[e-1])
now = e-1
ans = []
ans.append(e-1)
while True:
    ans.append(back_lst[now])
    now = back_lst[now]
    if now == s-1:
        break

print(len(ans))
for i in range(len(ans)-1,-1,-1):
    print(ans[i]+1, end = ' ')
