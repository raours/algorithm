import sys
from collections import deque
# 1. 입력 받기
input = sys.stdin.readline

n,m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]


def bfs(sr,sc,idx):
    q = deque()
    q.append((sr,sc))
    visit[sr][sc] = True
    lst[sr][sc] = idx

    while q:
        cr,cc = q.popleft()

        for i in range(4):
            nr,nc = cr+dr[i], cc+dc[i]
            if 0<= nr < n and 0<=nc<m and \
                    visit[nr][nc] == False and lst[nr][nc] == 1:
                q.append((nr,nc))
                visit[nr][nc] = True
                lst[nr][nc] = idx

def bfs2(sr,sc,now):
    dq = deque()
    for i in range(4):
        dq.append((sr,sc,i,0))

    while dq:
        cr,cc,d,cnt = dq.popleft()
        nr,nc = cr + dr[d], cc + dc[d]
        if nr<0 or nr>=n or nc<0 or nc>=m:
            continue
        if lst[nr][nc] == 0: #바다면 다리 설치 ok
            dq.append((nr,nc,d,cnt+1))
        elif lst[nr][nc] != now: #다른 섬이랑 만났음
            if cnt >= 2:
                bridges.append((cnt,now,lst[nr][nc]))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

#bfs로 각 섬에 번호 표시
idx = 1
visit = [[False]*m for _ in range(n)]
bridges = []
for i in range(n):
    for j in range(m):
        if visit[i][j] == False and lst[i][j] == 1:
            bfs(i,j,idx)
            idx += 1

#가능한 모든 다리 확인
for i in range(n):
    for j in range(m):
        if lst[i][j] != 0:
            bfs2(i,j,lst[i][j])

#크루스칼 알고리즘
bridges.sort()
parent = [i for i in range(idx)]

ans = 0
tmp = 0
for l,x,y in bridges:
    if find(x) != find(y):
        union(x,y)
        ans += l
        tmp += 1

if tmp != idx-2:
    print(-1)
else:
    print(ans)

