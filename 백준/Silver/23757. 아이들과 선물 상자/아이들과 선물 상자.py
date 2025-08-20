'''
2025.8.20
'''
import sys
import heapq
input = sys.stdin.readline


hq = []
n,m = map(int, input().split())
gift = [ -int(x) for x in input().split()]
heapq.heapify(gift)
kids = list(map(int, input().split()))
ans = 1
for num in kids:

    if -gift[0] >= num:
        heapq.heapreplace(gift, - (-gift[0] - num))
        # y = -heapq.heappop(gift)
        # heapq.heappush(gift, -(y-num))
    else: #선물 못 가져감
        ans = 0
        break
print(ans)

