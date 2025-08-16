'''
2025.8.16
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([num for num in range(1,n+1)])

while len(q)>1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q[0])
