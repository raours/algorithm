import sys
from collections import deque

input = sys.stdin.readline

def dfs(n):
    print(n, end= ' ')
    visited[n]=1
    for i in arr2[n]:
        if visited[i]==0:
            dfs(i)
    
def bfs(n):
    visited[n]=1
    q = deque([n])
    while q:
        v = q.popleft()
        print(v,end=' ')
        for i in arr2[v]: 
            if visited[i] ==0:
                q.append(i)   
                visited[i] =1 
            

N, M, V = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
arr2 = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    arr2[arr[i][0]].append(arr[i][1])
    arr2[arr[i][1]].append(arr[i][0]) 

#작은 번호부터 방문
for i in range(1, N+1):
    arr2[i].sort()


dfs(V)
print()
visited = [0]*(N+1)
bfs(V)