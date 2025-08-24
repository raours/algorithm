'''
2025.8.24
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    n_set = set(map(int, input().split()))
    m = int(input())
    m_lst = list(map(int, input().split()))

    for num in m_lst:
        if num in n_set:
            print(1)
        else:
            print(0)