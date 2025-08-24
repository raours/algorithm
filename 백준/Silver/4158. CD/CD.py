'''
2025.8.24
'''
import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if (n,m) == (0,0):
        break
    n_set = set(int(input()) for _ in range(n))
    m_set = set(int(input()) for _ in range(m))
    
    print(len(n_set&m_set))