from collections import deque
import sys
input = sys.stdin.readline

que  = deque([])
T = int(input())
for _ in range(T):
    N = input().split()
    if N[0]=='push':
        que.append(N[1])
    elif N[0]=='front':
        if len(que) !=0:
            print(que[0])
        else: 
            print(-1)
    elif N[0]=='back':
        if len(que) !=0:
            print(que[-1])
        else: 
            print(-1)
    elif N[0] =='size':
        print(len(que))
    elif N[0] =='empty':
        if len(que)==0:
            print(1)
        else:
            print(0)
    else:
        if len(que) !=0:
            print(que.popleft())
        else: 
            print(-1)
    


