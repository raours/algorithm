'''
2025.9.21
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
con = [0]*(n+1) #진입차수 저장할 배열
ans = []

for _ in range(m):
    temp = list(map(int, input().split()))
    for i in range(2,len(temp)):
        con[temp[i]] += 1
        lst[temp[i-1]].append(temp[i])

q = deque()
for i in range(1,n+1):
    if con[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    ans.append(cur)

    for nxt in lst[cur]:
        con[nxt] -= 1
        if con[nxt] == 0:
            q.append(nxt)

if len(ans) == n: #가능
    for a in ans:
        print(a)
else:
    print(0)