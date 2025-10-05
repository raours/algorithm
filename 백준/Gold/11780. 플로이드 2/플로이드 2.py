import sys
input = sys.stdin.readline

INF = 10**15
n = int(input().strip())
m = int(input().strip())

# 거리/경유지 행렬
dist = [[INF]*(n+1) for _ in range(n+1)]
route = [[0]*(n+1) for _ in range(n+1)]   # route[i][j] = i->j 최단경로의 중간 경유지 k (없으면 0)

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

# Floyd–Warshall
for k in range(1, n+1):
    for i in range(1, n+1):
        if dist[i][k] == INF:
            continue
        for j in range(1, n+1):
            if dist[k][j] == INF or i == j:
                continue
            new_cost = dist[i][k] + dist[k][j]
            if dist[i][j] > new_cost:
                dist[i][j] = new_cost
                route[i][j] = k

# 최소 비용 행렬 출력
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append('0' if dist[i][j] == INF else str(dist[i][j]))
    print(' '.join(row))

# 경로 복원 (재귀)
def get_path(i, j):
    k = route[i][j]
    if k == 0:              # 더 이상 쪼갤 경유지 없음 (직행)
        return [i, j]
    left = get_path(i, k)   # [i, ... , k]
    right = get_path(k, j)  # [k, ... , j]
    return left[:-1] + right  # k 중복 제거

# 경로 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j or dist[i][j] == INF:
            print(0)
        else:
            path = get_path(i, j)
            print(len(path), *path)
