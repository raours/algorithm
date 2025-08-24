'''
2025.8.24
이분 탐색으로
'''
import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = n
ans = n
while start<=end:
    mid = (start+end) // 2

    if mid**2 >= n:
        ans = mid
        end = mid-1
    else:
        start = mid + 1

print(ans)