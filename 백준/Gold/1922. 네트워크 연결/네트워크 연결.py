import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        p[y] = x
    else:
        p[x] = y

n = int(input())
m = int(input())

ans = 0
lst = [list(map(int,input().split())) for _ in range(m)]
lst.sort(key = lambda x: x[2])

p = list(range(n+1))
cnt = 0
for i in range(m):
    
    a, b, cost = lst[i]
    if a==b:
        continue
    if find(a) == find(b): #cycle
        continue
    
    union(a,b)
    ans += cost
    cnt += 1

    if cnt == n-1:
        break

print(ans)


