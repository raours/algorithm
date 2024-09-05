import sys
#sys.stdin = open("input3.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y, tmp, cnt):
    global result 
    if cnt ==4:
        result = max(result, tmp)
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            #tmp += lst[nx][ny] #이렇게 하면 dfs()돌아와서 tmp값을 다시 쓸 때 문제가 됨
            dfs(nx, ny, tmp+lst[nx][ny], cnt+1) # tmp+lst[nx][ny] 이렇게 다음 dfs()에 넘겨주기
            visited[nx][ny] = 0

def other(x,y):
    global result
    tmp = lst[x][y]
    arr =[]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            arr.append(lst[nx][ny])
    
    length = len(arr)
    if length ==4:
        arr.sort()
        arr.pop(0)
        result = max(result, tmp+sum(arr))
    elif length == 3:
        result = max(result, tmp+sum(arr))
    else:
        return


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i,j,lst[i][j],1)
        other(i,j)
        visited[i][j] = 0

print(result)