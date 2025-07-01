'''
2025.7.1
백준 : 벽 부수고 이동하기 3
'''
from collections import deque
import sys

N, M, K= map(int, input().split())

lst = [list(map(int, input().strip())) for _ in range(N)]

# dr = [0,0,-1,1,0]
# dc = [-1,1,0,0,0] #가만히 있는 것도 포함

dr = [0,0,-1,1]
dc = [-1,1,0,0] 

q = deque()
q.append((0,0,1,0,0)) #좌표, 거리, 부순 횟수, 낮
visit = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
visit[0][0][0] = True

def change_night(a):
    if a == 0:
        return 1
    else:
        return 0

answer = -1


while q:
    r,c,d,wall,night = q.popleft()

    if (r,c) == (N-1,M-1):
        answer = d
        break


    for i in range(4):
        nr,nc = r+dr[i], c+dc[i]

        if 0<=nr<N and 0<=nc<M:
            #벽이 아닐 때, 그냥 지나가면 됨
            if lst[nr][nc] == 0 and visit[nr][nc][wall] == False:
                q.append((nr,nc,d+1, wall, change_night(night)))
                visit[nr][nc][wall] = True

            #벽인데, 깰 수 있고(k번보다 적게 깸)
            if lst[nr][nc] == 1 and wall<K and visit[nr][nc][wall+1] == False:
                if night == 0: #낮이면 바로 깰 수 있음
                    q.append((nr,nc,d+1, wall+1, change_night(night)))
                    visit[nr][nc][wall+1] = True
                else: #밤이면, 낮이 될 때까지, 그 자리에서 한번 기다림!
                    # 이걸 그냥 기다린 애를 넣어주면 어떻게 될까..?
                    q.append((r,c,d+1, wall, change_night(night)))


print(answer)