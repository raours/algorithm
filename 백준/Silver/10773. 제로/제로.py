'''
2025.8.15
'''
import sys

input = sys.stdin.readline

k = int(input())
lst = []
for i in range(k):
    a = int(input().strip())
    if a == 0:
        lst.pop()
    else:
        lst.append(a)
print(sum(lst))