import sys
input = sys.stdin.readline

def find(x):
    # iterative + path halving
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

T = int(input())
out = []
for _ in range(T):
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]  # (x,y,r)

    parent = list(range(n))
    size = [1]*n

    # x정렬 + 안전한 조기 종료를 위한 suffix max r
    order = sorted(range(n), key=lambda i: pts[i][0])
    xs = [pts[i][0] for i in order]
    rs = [pts[i][2] for i in order]
    suf_max_r = [0]*n
    suf_max_r[-1] = rs[-1]
    for k in range(n-2, -1, -1):
        suf_max_r[k] = rs[k] if rs[k] > suf_max_r[k+1] else suf_max_r[k+1]

    for ii in range(n):
        i = order[ii]
        x1, y1, r1 = pts[i]
        for jj in range(ii+1, n):
            dx = xs[jj] - x1
            if dx > r1 + suf_max_r[jj]:   # 안전한 조기 종료
                break
            j = order[jj]
            x2, y2, r2 = pts[j]
            dy = y2 - y1
            s = r1 + r2
            if dx*dx + dy*dy <= s*s:
                union(i, j)

    groups = len({find(i) for i in range(n)})
    out.append(str(groups))

print("\n".join(out))
