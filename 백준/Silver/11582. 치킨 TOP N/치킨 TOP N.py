'''
2025.9.8
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
k = int(input())

temp = []
for i in range(0,n, n//k):
    temp.extend(sorted(lst[i:i+n//k]))
print(*temp)


