'''
2025.9.24
'''
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, k = map(int, input().split())
d = [INF]*(100001)

def solve(n):
    d[n] = 0 #시작점 최단거리는 0
    hq = []
    heapq.heappush(hq, (0,n)) #(최단거리, 노드번호)

    while hq:
        dis, now = heapq.heappop(hq)
        #방문 했던 노드인지 체크 : 방문했던 노드면, 이미 최단거리
        if dis > d[now]:
            continue #방문했으면 pass

        # *2 노드에 대해 확인
        nxt = now * 2

        if nxt < 100001 and d[nxt] > dis:  # now노드 거쳐서 가는게 더 빠르면,
            d[nxt] = dis  # 갱신
            if nxt == k:
                return
            heapq.heappush(hq, (d[nxt], nxt))
        
        # +1, -1 노드에 대해 확인
        for i in (1,-1):
            if 0<= now+i<100001:
                nxt = now+i

                if d[nxt] > dis+1: #now노드 거쳐서 가는게 더 빠르면,
                    d[nxt] = dis+1 #갱신
                    if nxt == k:
                        return

                    heapq.heappush(hq, (d[nxt], nxt))

       


solve(n)
print(d[k])