import sys
import heapq
input = sys.stdin.readline

N = int(input())
low = [] #최대힙
high = [] #최소힙
for _ in range(N):
    x = int(input())
    if len(low) == len(high):
        heapq.heappush(low, -x) #중간값은 항상 여기에!
    else:
        heapq.heappush(high, x)
    
    #high에 원소가 있어야 비교를 할 수 있음!
    if len(high) > 0 and high[0] < -low[0]: #low에 더 큰 값이 들어가있으면 switch
        left = -heapq.heappop(low)
        right = heapq.heappop(high)

        heapq.heappush(high, left)
        heapq.heappush(low, -right)

    print(-low[0])


