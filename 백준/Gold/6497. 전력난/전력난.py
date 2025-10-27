import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


while True:
    m,n = map(int, input().split())
    if (m,n) == (0,0):
        break
    lst = []
    sum_d = 0
    for _ in range(n):
        x,y,z = map(int, input().split())
        sum_d += z
        lst.append((z,x,y))

    lst.sort()
    parent = list(range(m+1))

    d = 0
    cnt = 0
    for l,a,b in lst:
        if cnt == m-1:
            break

        if find(a) != find(b):
            union(a,b)
            d += l
            cnt += 1

    print(sum_d-d)

