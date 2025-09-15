'''
2025.9.16
'''
import sys
input=sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = [0] * 100001

ans = 0
start = 0
end = 0
cur = 0

while end<n:
    num = lst[end]
    if cnt[num] < k:
        cnt[num] += 1
        cur += 1
        end += 1
    else:
        cnt[lst[start]] -= 1
        start += 1
        cur -= 1
    ans = max(ans, cur)
print(ans)