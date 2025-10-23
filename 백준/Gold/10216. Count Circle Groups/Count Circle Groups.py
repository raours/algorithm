import sys
sys.setrecursionlimit(10**5)
# 1. 입력 받기
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

t = int(input())
for i in range(1,t+1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    parent = [k for k in range(n)]
    for a in range(n):
        x1, y1, r1 = lst[a]
        for b in range(a+1,n):
            x2, y2, r2 = lst[b]

            if (x1-x2)**2 + (y1-y2)**2 <= (r1+r2)**2: #범위 내이면,
                union(a,b)

    for num in range(n):
        find(num)
    print(len(set(parent)))