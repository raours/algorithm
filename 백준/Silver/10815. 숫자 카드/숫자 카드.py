'''
2025.8.22
'''
import sys
input = sys.stdin.readline

n = int(input())
n_lst = set(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))

ans = []
for num in m_lst:
    if num in n_lst:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)
