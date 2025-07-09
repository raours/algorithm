'''
2025.7.7 // 7.9
백준 : 2048(Easy)
'''
import sys
from copy import deepcopy

input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

#합쳐지는 로직
#왼쪽으로 가는 방향이면,
def move_left(board):
    for i in range(n):
        cursor = 0
        for j in range(1,n):
            if board[i][j] != 0: #0이 아닌 숫자만 이동시켜야하니까! 이걸 꼭! 걸러줘야함
                temp = board[i][j]
                board[i][j] = 0 # 얘는 옆으로 밀거나 못 밀면 다시 그대로 갱신될 예정
                if temp == board[i][cursor] : #합쳐
                    board[i][cursor] *= 2
                    cursor += 1 #한번 합쳐진 애들은 더이상 건들지 않아야 하므로! cursor이동
                elif board[i][cursor] == 0: #빈칸
                    board[i][cursor] = temp  #쭉 왼쪽으로 밀어!
                else: #다른 숫자면,
                    cursor += 1 #놓일 수 있는 그 바로 옆으로!
                    board[i][cursor] = temp

    return board
            
    
#오른쪽으로 가는 방향이면,
def move_right(board):
    for i in range(n):
        cursor = n-1
        for j in range(n-2,-1,-1):
            if board[i][j] != 0: #0이 아닌 숫자만 이동시켜야하니까! 이걸 꼭! 걸러줘야함
                temp = board[i][j]
                board[i][j] = 0 # 얘는 옆으로 밀거나 못 밀면 다시 그대로 갱신될 예정
                if temp == board[i][cursor] :
                    board[i][cursor] *= 2
                    cursor -= 1 #한번 합쳐진 애들은 더이상 건들지 않아야 하므로! cursor이동
                elif board[i][cursor] == 0: #빈칸
                    board[i][cursor] = temp  #쭉 오른쪽으로 밀어!
                else: #다른 숫자면,
                    cursor -= 1 #놓일 수 있는 그 바로 옆으로!
                    board[i][cursor] = temp

    return board

#위쪽으로 가는 방향이면,
def move_up(board):
    for j in range(n):
        cursor = 0
        for i in range(1,n):
            if board[i][j] != 0: #0이 아닌 숫자만 이동시켜야하니까! 이걸 꼭! 걸러줘야함
                temp = board[i][j]
                board[i][j] = 0 # 얘는 옆으로 밀거나 못 밀면 다시 그대로 갱신될 예정
                if temp == board[cursor][j] : #커서 이번엔 행이다!
                    board[cursor][j] *= 2
                    cursor += 1 #한번 합쳐진 애들은 더이상 건들지 않아야 하므로! cursor이동
                elif board[cursor][j] == 0: #빈칸
                    board[cursor][j] = temp  #쭉 위쪽으로 밀어!
                else: #다른 숫자면,
                    cursor += 1 #놓일 수 있는 그 바로 옆으로!
                    board[cursor][j] = temp

    return board


#아래쪽으로 가는 방향이면,
def move_down(board):
    for j in range(n):
        cursor = n-1
        for i in range(n-2,-1,-1):
            if board[i][j] != 0: #0이 아닌 숫자만 이동시켜야하니까! 이걸 꼭! 걸러줘야함
                temp = board[i][j]
                board[i][j] = 0 # 얘는 옆으로 밀거나 못 밀면 다시 그대로 갱신될 예정
                if temp == board[cursor][j] : #합쳐
                    board[cursor][j] *= 2
                    cursor -= 1 #한번 합쳐진 애들은 더이상 건들지 않아야 하므로! cursor이동
                elif board[cursor][j] == 0: #빈칸
                    board[cursor][j] = temp  #쭉 아래쪽으로 밀어!
                else: #다른 숫자면,
                    cursor -= 1 #놓일 수 있는 그 바로 옆으로!
                    board[cursor][j] = temp

    return board

answer = 0

def dfs(dep,arr): #변수 겹치는 거 잘 보기!
    global answer
    if dep == 5: #dep이 5이면, 즉 5번 이동 완료한 경로면
        for i in range(n): #최대값 체크하고 리턴하라
            for j in range(n):
                if arr[i][j] > answer:
                    answer = arr[i][j]
        return

    for idx in range(4): #상하좌우 이동할것!
        # 같은 배열에 대해 상하좌우 이동이니까, deepcopy로 이전 배열 보존
        cp_arr = deepcopy(arr)
        
        if idx == 0: #왼
            dfs(dep+1, move_left(cp_arr))
        elif idx == 1: #오
            dfs(dep+1, move_right(cp_arr))
        elif idx == 2: #위
            dfs(dep+1, move_up(cp_arr))
        elif idx == 3: #아래
            dfs(dep+1, move_down(cp_arr))
        

dfs(0,lst)
print(answer)




