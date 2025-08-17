'''
2025.8.17
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque([num for num in range(1,n+1)])

ans = []
while len(q)>1:
    ans.append(q.popleft()) #맨 위 한장 버리고
    q.append(q.popleft())

ans.append(q[0]) # n = 1일 때도, 이걸로 출력 가능하게 됨!
print(*ans)

