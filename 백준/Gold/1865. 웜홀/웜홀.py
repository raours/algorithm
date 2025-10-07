'''
2025.10.7
'''
import sys
input = sys.stdin.readline

INF = int(1e9)

def bf(start):
    dist[start] = 0

    for i in range(n): #n번의 반복에 대해,
        for j in range(len(lst)): #모든 간선을 돌아보며 확인
            cur, nxt, tt = lst[j]

            if dist[cur]+tt <dist[nxt]:
                dist[nxt] = dist[cur]+tt

                if i == n-1: #이때도 갱신이 일어나면 -> 음수사이클 존재
                    return True
    return False


#입력 받기
T = int(input())
for _ in range(T):
    n,m,w = map(int, input().split())
    lst = []
    for _ in range(m):
        s,e,t = map(int, input().split())
        lst.append((s,e,t)) #도로엔 방향이 없다고 함
        lst.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        lst.append((s, e, -t))
    
    dist = [0]*(n+1) #음수 사이클만 볼거니까 양수 루트는 필요없음
    #시작 지점에 다시 돌아왔을 때, 출발 이전 시간이려면
    #음수사이클이 있어야 가능!
    if bf(1): #아무지점에서 시작해서 음수 사이클 있는지만 확인하면 된다!
        print('YES')
    else:
        print('NO')