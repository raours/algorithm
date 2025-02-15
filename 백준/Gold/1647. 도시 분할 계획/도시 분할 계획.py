#도시 분할 계획 문제
#크루스칼 알고리즘

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

N, M = map(int, input().split())
edges = []
for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort() # 간선 비용 기준 오름차순 정렬


parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i #자기를 루트 노드로 초기화

result = 0 #유지비
last = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += c
        last = c #가장 큰 유지비(나중에 빼면 -> 2개의 마을이 되는 것)

print(result - last)