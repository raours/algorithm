import sys
from collections import deque
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
#R, B 좌표 저장하기
board  = []


for i in range(N):
    board.append(list(input()))
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

dx = [0,0,-1,1] #동서북남
dy = [1,-1,0,0]

def move(x,y,dx,dy):
    # 현재 구멍에 빠지지 않았고 다음칸이 장애물이 아닐 때까지
    # 이동
    mcnt = 0
    while board[x][y] != 'O' and board[x+dx][y+dy] != '#':
        x += dx
        y += dy
        mcnt +=1 #그 방향으로 몇칸 갔는지
    return x, y, mcnt


def bfs(rx, ry, bx, by): #R좌표랑 B좌표를 가져와서 
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited = [(rx, ry, bx, by)]
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        #10번 초과면 -1 return
        if cnt >10:
            return -1

        for i in range(4):
            rnx, rny, rm = move(rx,ry,dx[i],dy[i])
            bnx, bny, bm = move(bx,by,dx[i],dy[i])
                
            #파랑이 구멍에 빠지면
            if board[bnx][bny] == 'O':
                continue  #실패한 경우이기 때문에 무시
            
            if board[rnx][rny] == 'O':
                return cnt

            #같은 자리에 있는 경우
            if rnx == bnx and rny == bny:
                if rm > bm:
                    rnx -=dx[i]
                    rny -=dy[i]
                else:
                    bnx -=dx[i]
                    bny -=dy[i]

            if (rnx, rny, bnx, bny) not in visited:
                #방문 처리해주고
                visited.append((rnx, rny, bnx, bny))
                #q에 추가하고 cnt를 1증가시키기
                q.append((rnx, rny, bnx, bny, cnt+1))
    return -1    

print(bfs(rx, ry, bx, by))
            