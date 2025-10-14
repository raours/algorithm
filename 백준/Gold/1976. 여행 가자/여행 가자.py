'''
2025.10.14
'''

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]



def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
m = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

travel = list(map(int, input().split()))
parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j] == 1: #연결되어 있으면,
            union(i,j)

target = find(travel[0]-1)
flag = True
for i in range(1,m):
    if find(travel[i]-1) != target:
        print('NO')
        flag = False
        break

if flag:
    print('YES')