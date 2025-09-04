'''
2025.9.4
'''
import sys

n = int(input())
lst = [int(input()) for _ in range(n)]

lst.sort(reverse=True) #내림차순 정렬

for i in range(n):
    lst[i] = lst[i]*(i+1)
print(max(lst))

