'''
2025.9.18
'''
import sys
input=sys.stdin.readline

n = int(input())

lst = [0] *(n+1)
lst[1] = 1

for i in range(2,n+1):
    lst[i] = lst[i-1] + lst[i-2]
print(lst[n])