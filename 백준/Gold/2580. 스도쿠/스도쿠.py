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
flag = [0]*n


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
                

def check_done():
    for i in range(n):
        if flag[i] == 0:
            return False
    return True

def dfs(idx,cnt):
    global board
    #종료조건 : 전부 맞혔으면,
    if idx == n and check_done():
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = " ")
            print() 
        exit()

    r,c = posi[idx]
    for num in range(1,10):
        #여기에서 체크를 해야함 num이 들어가도 되는지 안되는지
        if check(r,c,num):
            board[r][c] = num
            flag[idx] = 1
            dfs(idx+1,cnt+1) #그 칸에 넣었다 뺐다 하며(백트래킹)
            board[r][c] = 0
            flag[idx] = 0  


dfs(0,0)
           
