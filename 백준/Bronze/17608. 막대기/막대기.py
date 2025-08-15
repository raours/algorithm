'''
2025.8.15
'''
import sys

input = sys.stdin.readline
n = int(input())
n_lst = [int(input()) for _ in range(n)]

ans = 1
last = n_lst[-1]
for i in range(n-2, -1, -1):
    if last<n_lst[i]:
        ans += 1
        last = n_lst[i]
print(ans)