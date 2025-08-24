'''
2025.8.24
'''
import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

dic = {}
for num in n_lst:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for x in m_lst:
    if x in dic:
        print(dic[x], end = ' ')
    else:
        print(0, end = ' ')