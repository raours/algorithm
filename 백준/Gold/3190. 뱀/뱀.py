import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2  # 사과 위치에 2대입, 인덱스는 0,0부터 사과좌표는 1,1부터 시작이라 조정

T = int(input())
T_lst = []
for _ in range(T):
    X, C = input().split()
    T_lst.append((int(X), C))

D = 1 # 처음에 오른쪽을 향함
dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]
cnt =0

x = 0
y = 0
t = 0 #현재 시간
snake = [[0,0]]
board[x][y]=1

while True:

    nx = x+dx[D]
    ny = y+dy[D]
    if not (0<=nx<N and 0<=ny<N) or board[nx][ny]==1:
        t +=1
        break

    if board[nx][ny]==2:
        board[nx][ny] = 1
        snake.append([nx,ny])
    else:
        board[nx][ny] = 1
        snake.append([nx,ny])
        tail_x, tail_y = snake.pop(0)  # 꼬리 제거
        board[tail_x][tail_y] = 0  # 꼬리 위치 비우기

    x, y = nx, ny
    t +=1
    if cnt<T and t == T_lst[cnt][0]:
        if T_lst[cnt][1] == 'D':
            D = (D+1)%4 #시계방향
        else:
            D = (D-1)%4 #반시계방향
        cnt +=1

print(t)
