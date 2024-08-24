import sys
from collections import deque
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
chk = [[0]*N for _ in range(N)]
cnt = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    q = deque([(x,y)])
    combi = [(x,y)]
    chk[x][y] = 1
    total = lst[x][y]

    while q:
        cx, cy = q.popleft()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if 0<=nx<N and 0<=ny<N and chk[nx][ny] == 0: 
                if (L<=abs(lst[nx][ny] - lst[cx][cy])<=R):
                    q.append((nx,ny))
                    combi.append((nx,ny))
                    chk[nx][ny]=1
                    total += lst[nx][ny]

    if len(combi) > 1: #개방됐다면 인구수 재할당
        new = total//len(combi)
        for cx, cy in combi:
            lst[cx][cy] = new
        return True
    
    return False #개방되지 않았다면 False 리턴
                    

while True:
    t =0
    chk = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if chk[i][j] ==0:
                if bfs(i,j):
                    t += 1
    if t ==0: # 더이상 개방이 안되는 경우
        break
    cnt +=1

print(cnt)
