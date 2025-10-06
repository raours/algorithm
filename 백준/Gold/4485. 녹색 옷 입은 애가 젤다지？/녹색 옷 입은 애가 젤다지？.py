'''
2025.10.6
'''
import sys
import heapq
input = sys.stdin.readline

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def dijkstra():
    hq = []
    heapq.heappush(hq,(0,0,0))
    distance[0][0] = 0

    while hq:
        cost, r,c = heapq.heappop(hq)
        if cost > distance[r][c]: # 우선순위!
            continue

        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<n:
                if cost+lst[nr][nc] < distance[nr][nc]:
                    distance[nr][nc] = cost+lst[nr][nc]
                    heapq.heappush(hq,(distance[nr][nc],nr,nc))

idx = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    lst = [list(map(int,input().split())) for _ in range(n)]
    distance = [[1e10]*n for _ in range(n)]

    dijkstra()
    print(f"Problem {idx}: {distance[n-1][n-1]+lst[0][0]}")
    idx += 1
