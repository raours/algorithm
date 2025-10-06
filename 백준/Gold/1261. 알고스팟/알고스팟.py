'''
2025.10.6
다익스트라
'''
import sys
import heapq
input = sys.stdin.readline

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dijkstra():

    hq = []
    heapq.heappush(hq, (0,0,0))
    distance[0][0] = 0 #첫 시작점 거리 0

    while hq:
        cost,cr,cc = heapq.heappop(hq)

        if cost > distance[cr][cc]: #더 최소 벽 깨는게 아니면, 패스
            continue

        for i in range(4):
            nr,nc = cr+dr[i], cc+dc[i]
            if 0<=nr<n and 0<=nc<m: #범위 안이면,
                if cost+lst[nr][nc] < distance[nr][nc]: #더 최소 벽 깨기면,
                    distance[nr][nc] = cost+lst[nr][nc]
                    heapq.heappush(hq,(distance[nr][nc],nr,nc))

m,n = map(int,input().split())
lst = [list(map(int,input().strip())) for _ in range(n)]
distance = [[1e10]*m for _ in range(n)]

dijkstra()
print(distance[n-1][m-1])
