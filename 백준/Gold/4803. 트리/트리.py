import sys
from collections import deque

# 1. 입력 받기
input = sys.stdin.readline

def find(a):
    if lst[a] != a:
        lst[a] = find(lst[a])
    return lst[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a<b:
        lst[b] = a
    else:
        lst[a] = b

idx = 1
while True:
    n,m = map(int,input().split()) 
    if (n,m) == (0,0):
        break
    lst = [i for i in range(n+1)]
    lines = [list(map(int,input().split())) for _ in range(m)]
    cycle = set()
    flag = True
    for i in range(m):
        x,y = lines[i]
        
        if find(x) == find(y):
            #사이클 발생해도 끝까지 돌며, 다른 트리가 있는지 확인해야함!
            cycle.add(find(x))
        
        union(x,y)
    
    final_cycle = set()
    for c in cycle:
        final_cycle.add(find(c))

    if flag:
        ans = set()
        for i in range(1,n+1):
            ans.add(find(i))
        final_ans = ans - final_cycle

        if len(final_ans) == 1:
            print(f"Case {idx}: There is one tree.")
        elif len(final_ans) == 0:
            print(f"Case {idx}: No trees.")
        else:
            print(f"Case {idx}: A forest of {len(final_ans)} trees.")
    idx += 1
