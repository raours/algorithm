'''
2025.8.18
'''
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
q = deque([num for num in range(1, n+1)])

t = 1
while len(q) > 1:
    x = (t**3)%len(q)
    for i in range(x): #x번 pop하고 마지막에 pop되는 애가 out
        if i == x-1:
            q.popleft()
        else:
            q.append(q.popleft())
    if x == 0: #나머지가 0 이면,
        q.pop()
    t += 1
print(q[0])

