import sys 
sys.setrecursionlimit(100000) 

N = int(input())
board = [list(input()) for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]


def dfs(si, sj): #색약 x
    for i in range(4):
        ni = si +di[i]
        nj = sj +dj[i]
        if 0<=ni<N and 0<=nj<N and visit[ni][nj] ==False:
            if board[ni][nj] == board[si][sj]:
                visit[ni][nj] = True
                dfs(ni,nj)

def dfs2(si,sj, num):
        #색약 o
        for i in range(4):
            ni = si + di[i]
            nj = sj + dj[i]
            if 0<=ni<N and 0<=nj<N and visit2[ni][nj] ==False:
                if num == 1 and (board[ni][nj] == 'R' or board[ni][nj] =='G'):
                    visit2[ni][nj] = True
                    dfs2(ni,nj,1)
                elif num==2 and board[ni][nj] == 'B':
                    visit2[ni][nj] = True
                    dfs2(ni,nj,2)



visit = [[False]*N for _ in range(N)]
visit2 = [[False]*N for _ in range(N)]

flag = 0
flag2 = 0
for i in range(N):
    for j in range(N): #다 돌면서 찾아
        if visit[i][j] == False:
            flag +=1
            visit[i][j] = True
            dfs(i,j)

for i in range(N):
    for j in range(N):
        if visit2[i][j] == False:
            flag2 +=1
            if board[i][j] == 'R' or board[i][j] == 'G':
                #print(board[i][j])
                visit2[i][j] = True
                dfs2(i,j,1)

            elif board[i][j] == 'B':
                visit2[i][j] = True
                dfs2(i,j,2)


print(flag)
print(flag2)
