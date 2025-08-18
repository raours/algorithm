'''
2025.8.18
'''
import sys
import heapq
input = sys.stdin.readline

hq = []

n = int(input())

#heapq 사용법 복습!
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(hq) > 0:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, x)
