'''
2025.8.20
'''
import sys
import heapq
input = sys.stdin.readline


n = int(input()) # 방문한 횟수
hq = []
for _ in range(n):
    st = input()
    if st[0] == '0':
        # 아이들 방문
        if len(hq) == 0:
            print(-1)
        else:
            print(-heapq.heappop(hq))
    else:
        #거점지 방문
        lst = list(map(int, st[2:].split()))

        for a in lst:
            heapq.heappush(hq, -a)
