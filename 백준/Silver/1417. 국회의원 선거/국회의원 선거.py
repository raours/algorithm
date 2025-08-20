'''
2025.8.20
'''
import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    target = int(input())
    temp = target
    other = [int(input()) for _ in range(n-1)]
    other.sort(reverse =True)
    while True:
        if other[0] >= target:
            target += 1
            other[0] -= 1
            other.sort(reverse=True)
        else: break
    print(target-temp)

