from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0,0))
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1
    
    while q:
        cr,cc = q.popleft()
        for dr,dc in ((0,1),(0,-1),(1,0), (-1,0)):
            nr, nc = cr+dr, cc+dc
            if 0<=nr<n and 0<=nc<m and visit[nr][nc] == 0 and maps[nr][nc] == 1:
                q.append((nr,nc))
                visit[nr][nc] = visit[cr][cc]+1
                
    if visit[n-1][m-1] == 0:
        return -1

    else:
        return visit[n-1][m-1]