import sys

# 1. 입력 받기
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
ans = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


truth = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(m)]
if truth[0] == 0: # 모든 파티 가능
    print(m)

else:

    for idx in range(m):  # every party
        tmp = lst[idx]
        for i in range(1, len(tmp)-1):
            union(tmp[i+1], tmp[i])

    #진실 아는 사람들의 루트 집합
    truth = truth[1:]
    truth_roots = set(find(x) for x in truth)


    for idx in range(m): #파티마다 가능한지 확인
        party = lst[idx][1:]
        flag = True
        for person in party:
            x = find(person)
            if x in truth_roots: #진실 사람 루트 중에 같은 루트라면
                flag = False
                break
        if flag:
            ans += 1

    print(ans)






