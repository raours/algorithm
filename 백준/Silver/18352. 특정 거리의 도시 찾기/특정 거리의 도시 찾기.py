import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

lst = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    lst[i].append(j)

distance = [-1]*(N+1)
distance[X] = 0

q = deque([X])

while q:
    a= q.popleft() 
    for b in lst[a]:
        if distance[b] == -1:
            distance[b] = distance[a]+1 
            q.append(b)

flag = False
for index in range(1, N+1):
    if distance[index] == K:
        print(index)
        flag = True

if flag == False:
    print(-1)
