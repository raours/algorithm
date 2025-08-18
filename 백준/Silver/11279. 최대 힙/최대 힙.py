'''
2025.8.18
'''
import sys
import heapq
input = sys.stdin.readline

hq = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(hq) > 0:
            print(-1 * heapq.heappop(hq))
        else:
            print(0)
    else:
        #최소 힙에 -x로 넣어주면 최대힙 구현가능!
        heapq.heappush(hq, -x)