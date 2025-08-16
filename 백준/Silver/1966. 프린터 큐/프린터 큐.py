'''
2025.8.16
'''
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    q = deque(list(map(int, input().split())))

    cnt = 0
    while q:
        x = q.popleft()
        if len(q) == 0 or x>=max(q): #인쇄 될 수 o
            if target == 0: #target이면,
                print(cnt + 1)
                break
            else: # 다른 숫자면,
                cnt += 1
                target -= 1
        else: #인쇄 될 수 x
            if target == 0: #target이면,
                target = len(q) #맨 뒤로 보낼거니까 인덱스 변경
            else: #target 아니면
                target -= 1
            q.append(x)
