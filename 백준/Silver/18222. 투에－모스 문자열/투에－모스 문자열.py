'''
2025.9.8
'''
import sys

input=sys.stdin.readline

k = int(input())

# 투에-모스 수열 점화식
# t(0) = 0
# t(2n) = t(n)
# t(2n+1) = 1-t(n)

def solve(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    elif idx%2 == 0:
        return solve(idx//2)
    else:
        return 1-solve(idx//2)


print(solve(k-1))

