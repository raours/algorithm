import sys
from collections import deque

# 1. 입력 받기
input = sys.stdin.readline

def find(a):
    if lst[a] != a:
        lst[a] = find(lst[a])
    return lst[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if cost[a]<cost[b]: #비용 더 적은 애를 루트노드로!
        lst[b] = a
    else:
        lst[a] = b

n,m,k = map(int, input().split())
cost = [0] + list(map(int, input().split()))

lst = [i for i in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    union(x,y)

ans = 0
for i in range(1,n+1):
    if i == find(i):
        #루트 노드면,
        ans += cost[i]
    
if k >= ans:
    print(ans)
else:
    print('Oh no')




