import sys
from collections import deque


def bfs():
    global result
    q = deque([(1,1)]) #1번노드부터 출발
    visited[1] = True #방문처리
    while q:
        now,cnt = q.popleft()
        if now == N:
            result = cnt
            print(cnt)
            exit()
        for next in graph[now]:
            if not visited[next]: #방문한 적이 없으면
                visited[next] = True #방문처리
                if next<N+1: #역을을 방문하는거라면
                    q.append((next, cnt+1)) #이 cnt는 now에 의해 연결되어 있는 next의 cnt가 +=1 되는 것이라 노드에 대해 cnt가 있어야함
                else: #하이퍼튜브를 방문하는거라면
                    q.append((next, cnt))


N, K, M = map(int, input().split())
graph = [[] for _ in range(N+1+M)] #노드들(역1~N, 하이퍼튜브N+1~N+M)의 간선 정보 // 인접리스트로 역과 하이퍼튜브를 이어서 저장
for i in range(1,M+1):
    lst = list(map(int, input().split()))
    graph[N+i] = lst #하이퍼튜브가 연결하는 역의 정보
    for j in graph[N+i]: #역에 연결된 하이퍼튜브 정보보
        graph[j].append(N+i)

visited = [False] * (N+1+M)

bfs() #1번 노드에서 시작
print(-1)
    
