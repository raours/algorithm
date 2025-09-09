'''
2025.9.10
'''
import sys
input=sys.stdin.readline


n = int(input())
m = int(input())

lst = list(map(int,input().split()))
ans = 0
for a in lst:
    b = m-a
    if b in lst:
        ans += 1
print(ans//2)

