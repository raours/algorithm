'''
2025.8.16
'''
import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = deque(map(int, input().split())) #대기 중인 트럭들
t = 0
q = deque([0]*w) # 다리 길이 만큼 0으로 채워 초기화
weight = 0

while truck or weight>0: #대기 중인 트럭이 있거나, 현재 다리 위에 트럭이 있으면 계속
    t += 1 #시간 증가

    # 1. 도달한 트럭 or 빈칸 빼기
    weight -= q.popleft()

    if truck and weight+truck[0] <= l: # 최대하중을 넘지 않는다면,
        q.append(truck[0]) #트럭 다리위로
        weight += truck[0]
        truck.popleft() #대기 중인 트럭에서 제외
    else:
        q.append(0) # 트럭을 못 올리면, 빈칸을 채워, 다리 길이 유지

print(t)