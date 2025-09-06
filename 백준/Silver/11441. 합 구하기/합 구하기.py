'''
2025.9.7
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = [0]+list(map(int, input().split()))

#누적합 구하기
for i in range(2,n+1):
    lst[i] += lst[i-1]

m = int(input())

for _ in range(m):
    i,j = map(int, input().split())
    print(lst[j]-lst[i-1])