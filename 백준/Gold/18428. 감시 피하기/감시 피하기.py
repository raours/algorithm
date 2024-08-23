import sys
from itertools import combinations
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

lst = []
T =[]
empty = []
N = int(input())

for i in range(N):
    lst.append(list(input().split()))
    for j in range(N):
        if lst[i][j] == 'T':
            T.append((i,j))
        if lst[i][j] == 'X':
            empty.append((i,j)) 

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def watch(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        while(0<=nx and nx<N and ny>=0 and ny<N):
            if lst[nx][ny] == 'S':
                return True
            if lst[nx][ny] == 'T':
                break
            if lst[nx][ny] == 'O':
                break   
            nx += dx[i]
            ny += dy[i]
    return False

    
def process():
    #선생님 위치에서 감지되는 학생 있는지 확인
    for x, y in T:
        if watch(x, y):
            return True
    return False


find = False
for data in combinations(empty, 3): #가능한 모든 조합에 대해서
    for x,y in data: #장애물 설치
        lst[x][y] = 'O'
    
    #성공 케이스 있으면 바로 break
    if not process():
        find  = True
        break

    for x,y in data: #장애물 회수
        lst[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')