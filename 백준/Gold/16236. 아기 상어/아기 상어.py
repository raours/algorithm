'''
백준 아기상어 문제
16236번
'''

import sys
from collections import deque
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

N = int(input())
shark = []
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(N):
        if board[i][j] == 9:
            shark.append((i,j,2))
            board[i][j] = 0



dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = 0
fish = 0

#bfs를 이용해서 가장 가까운 물고기들을 찾아내고
def bfs(shark):
    visited = [[False] * N for _ in range(N)] 
    x, y, size = shark[0]
    visited[x][y] = True
    q = deque([(x,y,0)])
    lst = []
    md = 500 #가장 가까운 거리
    while q:
        x, y, d = q.popleft()
        if d+1> md:
            continue
       
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<N and 0<=ny<N and (d+1)<=md and visited[nx][ny] == False: #범위 안에 있고 방문x
                if board[nx][ny] == 0 or board[nx][ny] == size: #이동만 가능한 곳이라면
                    #방문처리, q에 넣기
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = True
                
                
                elif board[nx][ny] < size: # 잡아먹을 수 있다면
                    #방문 처리
                    lst.append((nx,ny,d+1))
                    visited[nx][ny] = True
                    md = d+1
                    
    return lst

#먹을 물고기가 없을 때까지 반복
while True:
    
    lst = bfs(shark)
    size = shark[0][2]
    #잡아먹을 물고기가 없으면
    if not lst:
        break

    #잡아먹을 물고기가 하나이상이면
    #거리, 가장 위, 왼쪽순으로 정렬
    lst.sort(key=lambda x: (x[2], x[0], x[1])) 
    
    #잡아먹게 되면 아기 상어 위치,아기상어 크기, 걸린시간 바뀌고 board에 0으로 바뀌고 
    fish +=1
    if fish >= size:
        size += 1
        fish = 0

    nx, ny, d = lst[0]
    result += d
    board[nx][ny] = 0  # 물고기 먹었으니 빈칸으로
    shark = [(nx, ny, size)] 

print(result)

