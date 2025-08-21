'''
2025.8.21
heapq 사용
'''
import sys
import heapq
from collections import deque
input = sys.stdin.readline


n,m = map(int, input().split())
park = [0]
park.extend([int(input()) for _ in range(n)])
car = [0]
car.extend([int(input()) for _ in range(m)])
q = deque()

ans = 0
hq = [a for a in range(1,n+1)]
parked = [-1] * (m+1)

def parking():
    global ans
    y = q.popleft()  # 대기열에 있는 처음 차 pop
    num = heapq.heappop(hq)  # 주차할 주차장 번호
    ans += car[y] * park[num]
    parked[y] = num  # 주차한 주차장 번호 기억

for _ in range(m*2):
    x = int(input()) #차 번호
    if x > 0: # 주차하기
        q.append(x) #대기열 입장
        if len(hq)>0: # 주차장 빈 곳 있으면,
            parking()
    else: #차빼기
        x = -x
        heapq.heappush(hq, parked[x]) #빈 주차장 번호 다시 삽입
        #대기열에 있는 차 있으면, 바로 주차시키기
        if len(q)>0:
            parking()


print(ans)



