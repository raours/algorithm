'''
2025.8.18
'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(hq) > 0:
            a,b = heapq.heappop(hq)
            print(a*b)
        else:
            print(0)
    elif x>0:
        heapq.heappush(hq, (abs(x), 1)) #첫번째 요소 기준 정렬
    else:
        heapq.heappush(hq, (abs(x), -1))

