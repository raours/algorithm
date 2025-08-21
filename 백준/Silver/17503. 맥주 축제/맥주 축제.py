'''
2025.8.21
'''
import sys
import heapq
input = sys.stdin.readline

n,m,k = map(int, input().split())
lst= [list(map(int, input().split())) for _ in range(k)]
lst.sort(key = lambda x: x[1]) #도수로 오름차순 정렬

beer = []
prefer = 0
flag = False
for i in lst: #도수가 작은 맥주부터 하나씩 마셔보며 비교
    heapq.heappush(beer, i[0]) #최소힙에 선호도를 넣어 관리 -> 선호도 부족하면, 가장 낮은 선호도 맥주 빼기
    prefer += i[0] #선호도 증가

    if len(beer) == n: #n개의 맥주를 마셨을 때,
        if prefer >= m: #선호도를 다 채웠으면,
            #현재의 도수가 답!
            print(i[1])
            flag = True
            break
        else:
            #선호도 다 못 채웠으면, 가장 낮은 선호도 맥주 빼기
            prefer -= heapq.heappop(beer)

if not flag:
    print(-1)



