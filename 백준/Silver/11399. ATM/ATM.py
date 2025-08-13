'''
2025.8.14
백준 : ATM
'''
import sys

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for t in lst:
    ans += t*(n)
    n -= 1
print(ans)