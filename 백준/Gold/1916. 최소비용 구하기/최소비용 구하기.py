'''
2025.9.24
'''
import sys
import heapq
input = sys.stdin.readline

INF = int(1e10) #최대값
n = int(input()) #도시: 노드
m = int(input()) #버스: 간선

lst = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,mon = map(int, input().split())
    lst[s].append((e,mon))
start, end = map(int, input().split())

d = [INF]*(n+1)
d[start] = 0 #시작점 최단거리는 0

hq = []
heapq.heappush(hq, (0,start)) #(최단거리, 노드번호)

while hq:
    dis, now = heapq.heappop(hq)
    #방문 했던 노드인지 체크 : 방문했던 노드면, 이미 최단거리
    if dis > d[now]:
        continue #방문했으면 pass

    for nxt in lst[now]: #이 노드에 연결된 모든 노드 확인
        #now 노드를 거쳐서 nxt 노드로 가는게 최단거리라면 갱신
        if d[nxt[0]] > dis + nxt[1]:
            d[nxt[0]] = dis + nxt[1]
            heapq.heappush(hq, (d[nxt[0]], nxt[0]))

print(d[end])
