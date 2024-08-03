'''bj15903.py
단순히 list를 쓰는 것은 정렬을 해줘야하기 때문에 비효율-> sort()의 시간 복잡도는 O(nlogn)
headq를 사용하면 push만 하면 되기 때문에 효율적 -> heap에서 삽입 연산의 시간 복잡도는 O(logn)

'''

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
heapq.heapify(lst)


for i in range(m):
    min1 = heapq.heappop(lst)
    min2 = heapq.heappop(lst)
    min_sum = min1+min2

    heapq.heappush(lst, min_sum)
    heapq.heappush(lst, min_sum)

print(sum(lst))