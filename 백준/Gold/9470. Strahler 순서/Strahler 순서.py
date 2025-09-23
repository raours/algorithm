'''
2025.9.23
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for idx in range(1,t+1):
    k, m, p = map(int, input().split())
    lst = [[] for _ in range(m+1)]
    ans = [0]*(m+1)
    done = [0] * (m+1)
    indegree = [0] * (m+1)

    for _ in range(p):
        a,b = map(int, input().split())
        lst[a].append(b)
        indegree[b] += 1 #진입차수 +1

    q = deque()
    for i in range(1, m+1):
        if indegree[i] == 0:
            q.append(i)
            ans[i] = 1 #순서 1임

    while q:
        cur = q.popleft()

        for nxt in lst[cur]:
            if ans[cur] == ans[nxt]: #같은 순서가 두번째이면,
                if done[nxt] == 0:
                    ans[nxt] += 1
                    done[nxt] = 1 #두개 이상이면 순서: i+1
            elif ans[cur] > ans[nxt]: # 더 큰 순서가 있으면,
                ans[nxt] = ans[cur]
                done[nxt] = 0 #초기화
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print(idx, ans[m])
