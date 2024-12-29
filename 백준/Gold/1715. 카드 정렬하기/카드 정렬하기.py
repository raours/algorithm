import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x = int(input())
    heapq.heappush(lst, x)
answer = 0

while True:  
    if len(lst) == 1:
        break
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    s = a+b
    answer += s
    heapq.heappush(lst, s)

print(answer)
