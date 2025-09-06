'''
2025.9.6
'''
import sys

input=sys.stdin.readline

n, k = map(int, input().split())
lst = [0]+list(map(int, input().split()))

#누적합
for i in range(2, n+1):
    lst[i] += lst[i-1]

ans = -1e10 #답이 -가 나올 수 있는 범위라면 0으로 시작하면 안됨!
for i in range(1, n-k+2):
    ans = max(ans, lst[i+k-1]-lst[i-1])
print(ans)

