import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

X = []
while len(X) < k:
    X += list(map(int, input().split()))
X = X[:k]


adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(n):
    nums = list(map(int, input().split()))
    if not nums:
        continue
    u = nums[0]
    for v in nums[1:]:
        adj[u].append(v)
        indeg[v] += 1

# 4) 위상정렬
q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
topo = []
while q:
    u = q.popleft()
    topo.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

# 5) 비트셋 DP: bitset[u] = u가 도달 가능한 노드들의 집합 (자기 자신 제외)
bitset = [0] * (n + 1)
for u in reversed(topo):         # 후행자부터 계산
    bs = 0
    for v in adj[u]:
        bs |= bitset[v]          # 자식의 도달 집합
        bs |= (1 << (v - 1))     # 직접 자식 v 추가
    bitset[u] = bs

# 6) X 중에서 도달 수 최대(동률이면 번호 최소)
best_id, best_cnt = None, -1
for x in sorted(X):
    c = bitset[x].bit_count()
    if c > best_cnt:
        best_cnt = c
        best_id = x

print(best_id)
