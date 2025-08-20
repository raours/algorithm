'''
2025.8.20
'''
import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    lst = list(map(int, input().split()))
    for a in lst:
        if len(hq)<n: #아직 힙이 최대길이 이하
            heapq.heappush(hq, a)
        else:
            #hq[0] 이랑 비교해서 더 크면, 힙에 넣기!
            if hq[0] < a:
                heapq.heappush(hq, a)
                heapq.heappop(hq) #작은 애는 빼서, 힙의 크기를 계속 n으로 유지

print(hq[0]) #heapq에는 큰 애들이 n개 들어있으며, hq[0]가 n번째 큰 수임!
