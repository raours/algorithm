'''
2025.8.14
백준 : 단어 정렬
'''
import sys

n = int(input())
lst = [input().strip() for _ in range(n)]

lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
print(*lst, sep='\n')