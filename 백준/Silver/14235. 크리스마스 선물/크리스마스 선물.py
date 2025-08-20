'''
2025.8.20
'''
import sys
import heapq
input = sys.stdin.readline


n = int(input()) # 방문한 횟수
hq = []
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        # 아이들 방문
        if len(hq) == 0:
            print(-1)
        else:
            print(-heapq.heappop(hq))
    else:
        for a in lst[1:]:
            heapq.heappush(hq, -a)
