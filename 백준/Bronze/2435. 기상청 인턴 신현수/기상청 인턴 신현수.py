'''
2025.9.4
'''
import sys

n,k = map(int, input().split())
lst = list(map(int, input().split()))

ans = -100 * (n+1) #온도의 범위! -100<= <=100
for start in range(n-k+1):
    ans = max(ans, sum(lst[start:start+k]))
print(ans)
