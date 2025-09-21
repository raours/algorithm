'''
2025.9.21
'''
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)] #학생마다 뒤에 있는 학생정보
con = [0]*(n+1) #진입차수 저장할 배열
for _ in range(m):
    x,y = map(int, input().split())
    con[y] += 1 #진입차수 +1
    lst[x].append(y)

q = deque()
for i in range(1,n+1):
    if con[i] == 0: #진입차수가 0인 곳부터 시작!
        q.append(i)
ans = []

while q:
    cur = q.popleft()
    ans.append(cur)

    for nxt in lst[cur]:
        con[nxt] -= 1 #연결되어 있는 간선 모두 끊기
        if con[nxt] == 0: #진입차수가 모두 0이 되었으면 큐에 추가
            q.append(nxt)

print(*ans)



