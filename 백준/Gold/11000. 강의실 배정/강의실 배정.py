import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

#각 강의실 끝나는 시간 넣을 heapq
roomTime = []
heapq.heappush(roomTime, lst[0][1])

for i in range(1,N):
    if roomTime[0]<=lst[i][0]:
        # 강의 시작 시간이 강의실 종료 시간보다 크거나 같으면 이어서 사용
        heapq.heappop(roomTime)
        heapq.heappush(roomTime, lst[i][1])

    else:
        heapq.heappush(roomTime, lst[i][1])
        
print(len(roomTime))