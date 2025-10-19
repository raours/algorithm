import sys
input = sys.stdin.readline

def find(x): #루트 노드 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b: #루트 노드인 이름이 다르면,
        parent[b] = a #루트노드 합쳐주고
        cnt[a] += cnt[b] #통일한 루트노드에 친구 수 합쳐 저장

    print(cnt[a])



T = int(input())
for i in range(T):
    parent = {}
    cnt = {} #친구 관계 수

    F = int(input())
    for _ in range(F):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            cnt[x] = 1
        if y not in parent:
            parent[y] = y
            cnt[y] = 1
        union(x,y)
