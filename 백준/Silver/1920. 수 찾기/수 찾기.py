'''
2025.8.14
백준 : 수 찾기
'''

import sys

n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

for i in range(m):
    if m_lst[i] in n_set: #set의 in 연산 시간 복잡도 : O(1)
        print(1)
    else:
        print(0)