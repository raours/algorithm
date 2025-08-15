'''
2025.8.15
'''
import sys

n = int(input())
lst = []
for idx in range(1,n+1):
    age, name = input().split()
    lst.append((int(age), idx, name))

lst.sort()
for i in range(n):
    print(lst[i][0], lst[i][2])
