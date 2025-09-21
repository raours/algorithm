'''
2025.9.22
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(n+1)]
con = [0]*(n+1) #진입차수 저장할 배열
t = [0]
for idx in range(1,n+1):
    temp = list(map(int, input().split()))
    t.append(temp[0]) #각 작업에 대한 시간
    if len(temp)>2: #선행 작업이 있으면,
        for i in range(2,len(temp)):
            con[temp[i]] += 1
            lst[idx].append(temp[i])

q = deque()
dp = [0] * (n+1)
for i in range(1,n+1):
    if con[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    dp[cur] = dp[cur]+t[cur] 

    for nxt in lst[cur]:
        con[nxt] -= 1
        dp[nxt] = max(dp[nxt],dp[cur]) #연결되어 있는 간선 끊을 때마다 update
        if con[nxt] == 0:
            q.append(nxt)

print(max(dp))

