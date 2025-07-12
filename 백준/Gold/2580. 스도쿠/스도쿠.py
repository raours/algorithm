'''
2025.07.12
백준 : 스토쿠
'''
import sys
from collections import deque

input = sys.stdin.readline

board = []
posi = []
for i in range(9):
    board.append(list(map(int, input().split())))
    for j in range(9):
        if board[i][j] == 0:
            posi.append((i,j))

n = len(posi)

def check(r,c,num):
    #가로일 땐, r고정
    for j in range(9):
        if board[r][j] == num:
            return False
    
    #세로
    for i in range(9):
        if board[i][c] == num:
            return False
    
    #사각형
    sr, sc = (r//3) * 3, (c//3) * 3
    for i in range(sr, sr+3):
        for j in range(sc, sc+3): #사각형 범위 돌며,
            if board[i][j] == num:
                return False
    
    return True
                

def dfs(idx):
    #종료조건 : 전부 맞혔으면,
    if idx == n: #어차피 check()로 들어가도 되는지 아닌지 계속 체크해서 넣기 때문에
        #idx == n 까지 온 거면 그 조건들을 다 만족시키고 모든 빈칸을 채웠다는 소리가 됨!
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit()

    r,c = posi[idx]
    for num in range(1,10):
        #여기에서 체크를 해야함 num이 들어가도 되는지 안되는지
        if check(r,c,num):
            board[r][c] = num
            dfs(idx+1)
            board[r][c] = 0


dfs(0)

          
