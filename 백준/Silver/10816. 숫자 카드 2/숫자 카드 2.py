'''
2025.8.24
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

cnt = Counter(n_lst)

print(' '.join(str(cnt.get(x, 0)) for x in m_lst))