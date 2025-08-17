'''
2025.8.16
'''
import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
t = 0
q = deque()
idx = 0

def cal_sum(que):
    temp = 0
    for i in range(len(que)):
        temp += que[i][0]
    return temp

done = [0] * n

def flag():
    for i in range(n):
        if done[i] == False:
            return True
    return False

while flag():
    t += 1 #시간 증가

    # 1. 도달한 트럭부터 빼기
    #큐에넣은 시각+w == t 면 빼야함
    if len(q)>0 and q[0][1]+w == t:
        done[q[0][2]] = 1
        q.popleft() # 건너감!

    if len(q)<w: #들어갈 자리가 있고,
        if idx < n and cal_sum(q)+truck[idx] <= l: # 최대하중을 넘지 않는다면,
            q.append((truck[idx],t,idx)) #무게, 들어온 시각
            idx += 1


print(t)