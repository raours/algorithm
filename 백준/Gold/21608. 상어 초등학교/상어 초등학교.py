'''
백준 상어 초등학교 문제
21608번
'''
import sys
from collections import deque
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N*N)]
board = [[0] * N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

#좋아하는 학생이 인접한 칸에 많은 지 확인
def check(n,x,y):
    friends = lst[n]
    num = 0
    empty = 0
    for i in range(4):
        nx, ny = x +dx[i], y +dy[i]
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in friends:
            num +=1 #좋아하는 학생 인접 갯수
        elif 0 <= nx < N and 0 <= ny < N and board[nx][ny] ==0:
            empty +=1

    position.append((x,y, num, empty))
    return

def cal():
    result = 0
    for x in range(N):
        for y in range(N):
            #각각의 칸마다 좋아하는 학생 있는지 확인, 만족도 계산
            num = 0
            lst2 = sorted(lst)
            friends = lst2[board[x][y]-1]
            for index in range(4):
                nx, ny = x +dx[index], y +dy[index]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in friends:
                    num +=1 #좋아하는 학생 인접 갯수
            if num == 1:
                result +=1
            elif num == 2:
                result += 10
            elif num == 3:
                result += 100
            elif num == 4:
                result += 1000
    return result


#학생 한명씩 모든 칸에 대해 검사 
for n in range(N*N):
    position = [] #가능한 위치 비우기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                check(n,i,j)
    
    position.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    x = position[0][0]
    y = position[0][1]
    
    board[x][y] = lst[n][0]
    visited[x][y] = True


print(cal())



