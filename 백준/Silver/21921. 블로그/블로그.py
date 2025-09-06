'''
2025.9.6
'''
import sys

input=sys.stdin.readline

n,x = map(int, input().split())
lst = list(map(int, input().split()))

#누적합 구하기
for i in range(1,n):
    lst[i] += lst[i-1]

ans = []
ans.append(lst[x-1])
for i in range(1,n-x+1):
    ans.append(lst[i+x-1]-lst[i-1])

num = max(ans)
if num == 0:
    print('SAD')
else:
    print(num)
    print(ans.count(num))