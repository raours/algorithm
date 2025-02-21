import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for num in range(T):
    n = int(input())
    #각 노드에 연결된 간선 정보 graph[a][b] : a-> b 간선
    graph = [[False] *(n+1) for _ in range(n+1)] 
    lst = list(map(int, input().split()))
    indegree = [0]*(n+1)
    #입력값을 토대로 간전 정보와 진입차수 초기화
    for i in range(n-1):
        for j in range(i+1, n):
            graph[lst[i]][lst[j]] = True
            indegree[lst[j]] += 1 # 진입차수 증가 

    m = int(input())
    #올해의 상대적 순위 정보 적용용
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[b][a]: #작년에 a가 b보다 낮은 순위였다면 // indegree[a] > indegree[b] 이렇게 하면 안됨, 진입차수는 계속 바뀌기 때문
            graph[a][b] = True
            graph[b][a] = False

            indegree[a] -= 1 #진입차수 -1 : a -> b로 바뀌기 때문
            indegree[b] += 1 #진입차수 +1 

        else:
            graph[a][b] = False
            graph[b][a] = True

            indegree[b] -= 1 
            indegree[a] += 1 
            


    #위상 정렬 알고리즘
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0: # 진입 차수 0인 것 큐에 넣기
            q.append(i)

    ans = [] #답을 담을 리스트 / 큐에서 pop된 순서로 출력한게 위상정렬 결과값값
    cycle = False #사이클 있는지 -> "IMPOSSIBLE"출력
    certain = True #정확한 순위가 정해지는지 -> "?"출력

    for _ in range(n): #팀 수만큼 수행하여 그 사이에 큐 안의 원소 개수 파악
        if len(q) == 0: #큐가 비어있으면 -> 사이클 발생
            cycle = True
            break
        if len(q) >1: #큐에 2개 이상 있으면 -> 경우의 수가 2개이상 발생
            certain = False
            break
        now = q.popleft()
        ans.append(now)
        # now 노드에 연결된 간선 제거 & 연결되어 있던 상대 노드의 진입차수 -1
        for i in range(1, n+1):
            if graph[now][i]:
                graph[now][i] = False
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif certain == False:
        print("?")
    else:
        for i in range(n):
            print(ans[i], end=" ")
        print()
