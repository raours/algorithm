import sys
import heapq
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


v, e = map(int,input().split())
hq = []
ans = 0

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

for _ in range(e):
    a,b,c = map(int,input().split())
    heapq.heappush(hq, (c,a-1,b-1))

p = list(range(v))
cnt = 0
for _ in range(e):
    if cnt == v-1:
        break

    cost, a, b = heapq.heappop(hq)

    if find(a) == find(b): #cycle
        continue
    
    union(a,b)
    ans += cost
    cnt += 1
print(ans)


