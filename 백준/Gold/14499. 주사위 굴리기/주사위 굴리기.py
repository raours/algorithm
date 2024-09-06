import sys
input = sys.stdin.readline

N, M, r, c, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]  # 주사위의 각 면 초기화 (밑, 윗, 오른, 왼, 앞, 뒤)

# 이동 방향: 동(1), 서(2), 북(3), 남(4)
dx = [0, 0, -1, 1]  # 동서북남
dy = [1, -1, 0, 0]

def move(num):
    # 주사위의 면을 이동에 따라 변경
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if num == 1:  # 동쪽
        dice[0], dice[1], dice[2], dice[3] = c, d, b, a

    elif num == 2:  # 서쪽
        dice[0], dice[1], dice[2], dice[3] = d, c, a, b

    elif num == 3:  # 북쪽
        dice[0], dice[1], dice[4], dice[5] = f, e, a, b

    elif num == 4:  # 남쪽
        dice[0], dice[1], dice[4], dice[5] = e, f, b, a

for i in range(n):
    num = order[i]
    nx = r + dx[num-1]
    ny = c + dy[num-1]
    
    # 범위를 벗어나면 무시
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    # 주사위를 이동
    move(num)
    
    # 주사위가 위치한 칸의 숫자 처리
    if board[nx][ny] == 0:
        board[nx][ny] = dice[0]  # 주사위 바닥면의 숫자를 칸에 복사
    else:
        dice[0] = board[nx][ny]  # 칸의 숫자를 주사위 바닥면에 복사
        board[nx][ny] = 0  # 칸의 숫자는 0으로 변경
    
    # 주사위의 윗면 출력
    print(dice[1])
    
    # 주사위 위치 갱신
    r, c = nx, ny
