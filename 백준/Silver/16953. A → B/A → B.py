'''
2025.9.4
'''
import sys
from collections import deque

a,b = map(int,input().split())

q = deque()
q.append((a,0))
flag = False
while q:
    cur,cnt = q.popleft()

    next1 = cur*2
    next2 = cur*10+1
    if next1 == b or next2 == b:
        print(cnt + 2)
        flag = True
        break
    elif next1 < b or next2 < b:
        q.append((next1, cnt+1))
        q.append((next2, cnt+1))

if not flag:
    print(-1)