import sys
import heapq

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
lst = []
for i in range(N):
    x,y,z = map(int, input().split())
    lst.append((i,x,y,z))

edges = []

#루트 노드를 자기 자신으로 초기화
parent = [0] * N
for i in range(N):
    parent[i] = i

for num in range(1,4):
    lst.sort(key=lambda x: x[num]) #각각의 축 기준 정렬
    for i in range(N-1):
        d = abs(lst[i][num]-lst[i+1][num]) #각 좌표끼리 뺐지 그럼 그게 d임 그걸 edges에 a,b랑 넣어 ,, lst[][num]을 통해 각 축에 대해 모두!
        heapq.heappush(edges, (d, lst[i][0], lst[i+1][0]))
        
        

result = 0
while edges:
    c, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b): #루트 노드가 다르면, 즉 아직 연결 안 되어 있으면
        #거리 짧은 순으로 정렬을 해놨기 때문에 빠른 거리로 차례차례 연결됨 이게 if문에서서 중복처리됨
        union(parent, a, b)
        result +=c
        
print(result)
