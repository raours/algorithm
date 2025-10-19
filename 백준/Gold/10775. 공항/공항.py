import sys

input = sys.stdin.readline

g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
ans = 0

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(p):
    num = int(input())

    if find(num) == 0: #더이상 갈 수 도킹 x
        break

    #도킹
    ans += 1
    union(num, parent[num]-1)
print(ans)