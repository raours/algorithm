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
            shark.append((i, j, 2))  # 상어 위치와 크기 초기화
            board[i][j] = 0  # 상어 위치는 빈칸으로

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
fish = 0

# bfs를 이용해서 가장 가까운 물고기를 찾아냄
def bfs(shark):
    x, y, size = shark[0]
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 체크하는 리스트
    q = deque([(x, y, 0)])  # 큐에 (x좌표, y좌표, 거리) 형태로 초기화
    visited[x][y] = True
    lst = []
    md = 500  # 가장 가까운 거리

    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:  # 범위 안에 있고, 방문하지 않은 곳
                if board[nx][ny] == 0 or board[nx][ny] == size:  # 이동 가능한 곳
                    q.append((nx, ny, d + 1))
                    visited[nx][ny] = True
                elif board[nx][ny] < size:  # 먹을 수 있는 물고기
                    lst.append((nx, ny, d + 1))
                    visited[nx][ny] = True
                    md = d + 1  # 가장 가까운 거리 갱신
    return lst

# 먹을 물고기가 없을 때까지 반복
while True:
    lst = bfs(shark)
    size = shark[0][2]

    # 잡아먹을 물고기가 없으면 종료
    if not lst:
        break

    # 잡아먹을 물고기가 하나 이상이면
    lst.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, 가장 위, 가장 왼쪽 순으로 정렬
    fish += 1
    if fish >= size:  # 상어 크기 증가 조건
        size += 1
        fish = 0

    # 상어 위치 및 보드 갱신
    nx, ny, d = lst[0]
    result += d
    board[nx][ny] = 0  # 물고기 먹었으니 빈칸으로
    shark = [(nx, ny, size)]  # 상어 위치 갱신

print(result)
