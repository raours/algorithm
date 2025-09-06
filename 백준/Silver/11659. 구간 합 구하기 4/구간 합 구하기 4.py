import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# ps[k] = arr[0] + ... + arr[k-1]
ps = [0] * (n + 1)
for k in range(1, n + 1):
    ps[k] = ps[k - 1] + arr[k - 1]

out = []
for _ in range(m):
    i, j = map(int, input().split())
    out.append(str(ps[j] - ps[i - 1]))

print('\n'.join(out))