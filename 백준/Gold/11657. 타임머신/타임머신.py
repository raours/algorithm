'''
2025.10.7
'''
import sys
input = sys.stdin.readline

INF = int(1e9)

#음수 간선 o, 최단경로 -> 벨만-포드!
def bf(start):
    distance[start] = 0 #시작 지점 초기화

    #모든 반복마다,
    for i in range(n):
        #모든 간선을 확인한다.
        for j in range(m):
            cur, nxt, cost = bus[j]
            #현재 간선 이용해서 갔을 때, 더 짧은 경우,
            if distance[cur] != INF and distance[nxt]>distance[cur]+cost:
                distance[nxt] = distance[cur] + cost

                #n번째 라운드에서도 값이 갱신되었다? -> 음수 순환 존재
                if i == n-1:
                    return False
    return True #음수 순환 없음


n,m = map(int,input().split())
bus = []

for _ in range(m):
    a,b,c = map(int,input().split())
    bus.append((a,b,c)) #모든 버스(간선)에 대한 정보 담는 배열열
distance = [INF] * (n+1)
if bf(1):
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])

else:
    print(-1) #음수순환 존재