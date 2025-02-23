import sys
from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    t = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for i in range(K):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())

    ans = t[:] #얕은 복사
    q = deque()
    for i in range(1,N+1):
        if indegree[i] == 0: #진입 차수 0인 건물 큐에 넣기
            q.append((t[i],i)) #건설할 때 걸리는 시간, 인덱스

    while q:
        time, now = q.popleft()
        
        for next in graph[now]: #연결된 노드에 대해 모두 계산
            indegree[next] -=1
            # now 건물까지의 건설시간+next 건물 건설 시간 vs 지금 저장되어있는 next건물까지의 건설시간 중에 더 오래걸리는 값으로 갱신
            ans[next] = max(ans[next], time+t[next]) 
            
            if indegree[next] == 0:
                q.append((ans[next], next))

    print(ans[W])
        
