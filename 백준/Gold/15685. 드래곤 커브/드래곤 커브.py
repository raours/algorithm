'''
2025.7.22 - 7.23
백준 : 드래곤 커브
'''
import sys
input = sys.stdin.readline
n = 101
dragon_n = int(input())

dragon = [list(map(int, input().split())) for _ in range(dragon_n)]
board = [[0]*(n+1) for _ in range(n+1)]
dx = [1,0,-1,0] #x좌표가 열
dy = [0,-1,0,1] #y좌표가 행

for i in range(dragon_n):
    x,y,d,g = dragon[i]
    board[x][y] = 1 # 초기 시작점
    if 0> x+dx[d] or x+dx[d] > n or 0> y+dy[d] or y+dy[d] > n:
        continue
    board[x+dx[d]][y+dy[d]] = 1 #초기 끝점
    ex, ey = x+dx[d], y+dy[d]
    dlst = [d]
    for j in range(g): #세대만큼 커브 진행!
    
        #끝 점, 나아갈 방향 리스트가 필요

        #나아갈 방향 리스트는 이전 세대의 
        # 방향리스트에서 뒤부터 하나씩 꺼내서 90도로 바꾸고
        temp = dlst
        for j in range(len(dlst)-1, -1, -1):
            sd = (dlst[j]+1)%4

            # 그리고 board에 그 방향대로 한칸씩 이동해나가며 1로 체크
            if 0> ex+dx[sd] or ex+dx[sd] > n or 0> ey+dy[sd] or ey+dy[sd]>n:
                break
            ex, ey = ex+dx[sd], ey+dy[sd] 
            board[ex][ey] = 1
            # 이전 방향리스트에 그 방향도 추가해야해
            temp.append(sd)
        dlst = temp #새로운 방향리스트로 바꿔주기


ans = 0
# 둘러쌓인 정사각형 개수 구하기
# (0,n-1)까지 돌면서 정사각형 1인지 확인
for i in range(n):
    for j in range(n):
        if board[i][j] ==1 and board[i+1][j+1] == 1 \
                and board[i+1][j] == 1 and board[i][j+1] ==1 :
            ans += 1

print(ans)


