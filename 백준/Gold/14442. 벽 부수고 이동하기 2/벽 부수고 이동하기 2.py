'''
2025.6.29
백준 : 벽 부수고 이동하기2
'''
from collections import deque
import sys

input = sys.stdin.readline
n,m,k = map(int, input().split())
lst  = [list(map(int,input().strip())) for _ in range(n)]


answer = 0

q = deque()
q.append((0,0,1,0)) #r,c,d,벽깼는지
visit = [[[False]*(k+1) for _ in range(m)] for _ in range(n)]
visit[0][0][0] = True

dr = [0,1,0,-1]
dc = [1,0,-1,0]
answer = -1
while q:
    r,c,d,wall = q.popleft()

    if (r,c) == (n-1,m-1):
        answer = d
        break
       
    
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<n and 0<=nc<m:
            #벽x
            if visit[nr][nc][wall] == False and lst[nr][nc] == 0:
                q.append((nr,nc,d+1,wall))
                visit[nr][nc][wall] = True
            
            # 벽o, 벽을 깰 수 있는 경우
            # -> 벽을 한번도 깬 적이 없어서 가능
            elif lst[nr][nc] == 1 and wall < k and visit[nr][nc][wall+1] == False:
                q.append((nr,nc,d+1,wall+1))
                visit[nr][nc][wall+1] = True

            # 벽o, 벽을 못깨는 경우 ->
            # 벽을 이미 깼거나, 벽을 안깨거나
            # pass
    

print(answer)    

