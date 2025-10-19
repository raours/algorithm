import sys

input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
lst = [list(map(int,input().split())) for _ in range(m)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: #사이클 발생!
        return True
    if x>y:
        parent[x] = y
    else:
        parent[y] = x
    return False


flag = False
for i in range(1,m+1):
    a,b = lst[i-1]

    if union(a,b):
        print(i)
        flag = True
        break

if not flag:
    print(0)