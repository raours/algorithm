'''
2025.9.10
'''
import sys
input=sys.stdin.readline



n, m = map(int,input().split())
n_lst = list(map(int,input().split()))
m_lst = list(map(int,input().split()))

n_lst.extend(m_lst)
n_lst.sort() #정렬부터!
print(*n_lst)

