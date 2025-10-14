'''
2025.10.14
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x: #루트노드가 아니라면,
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x) #루트 노드 찾기
    y = find(y)

    if x>y: #루트노트 갱신 (합집합)
        parent[x] = y
    else:
        parent[y] = x

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    num, a,b = map(int,input().split())
    if num == 0: #합집합
        union(a,b)
    else: #같은 집합인지
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
