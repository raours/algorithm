'''
2025.10.2
다익스트라
'''
import sys
import heapq
input = sys.stdin.readline

INF = 1e9
n,m,r = map(int,input().split())
items = [0]+list(map(int,input().split()))
lst = [[] for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int,input().split())
    lst[a].append((b,l))
    lst[b].append((a,l))


ans = 0
#각 지역에 대해 다익스트라!
for i in range(1,n+1):
    distance = [INF]*(n+1) #거리 초기화
    hq = []
    heapq.heappush(hq, (0,i))
    distance[i] = 0

    while hq:
        dist,now = heapq.heappop(hq)
        if distance[now] <dist: #이미 최단거리면,
            continue #pass
        for nxt in lst[now]:
            nxt_d = dist+nxt[1]
            if nxt_d < distance[nxt[0]]: #얘를 거쳐가는게 최단거리면,
                distance[nxt[0]] = nxt_d
                heapq.heappush(hq, (nxt_d, nxt[0]))

    #i지역에 대한 distance 완성
    tmp = 0
    for idx in range(1,n+1):
        if distance[idx]<=m: #갈 수 있는 지역이라면
           tmp += items[idx]
    ans = max(ans, tmp)


print(ans)
