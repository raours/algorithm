'''
2025.9.21
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
lst = [[] for _ in range(n+1)]
con = [0]*(n+1) #진입차수 저장할 배열
t = [0]
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    t.append(temp[0])

    # 먼저 세워져야하는 건물 조건이 있다면,
    if len(temp)>2:
        for j in range(1,len(temp)-1):
            con[i] += 1
            lst[temp[j]].append(i)

q = deque()
for i in range(1,n+1):
    if con[i] == 0: #진입차수가 0인 곳부터 시작!
        q.append((i,0))
ans = [0]*n

while q:
    cur, ct = q.popleft()
    nt = ct+t[cur]
    ans[cur-1] = nt

    for nxt in lst[cur]:
        con[nxt] -= 1 #연결되어 있는 간선 모두 끊기
        ans[nxt-1] = max(ans[nxt-1], nt)
        if con[nxt] == 0: #진입차수가 모두 0이 되었으면 큐에 추가
            q.append((nxt,ans[nxt-1]))
for num in ans:
    print(num)



