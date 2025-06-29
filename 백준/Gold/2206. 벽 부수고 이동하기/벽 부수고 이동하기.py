from collections import deque

n,m = map(int,input().split()) #행렬 크기 입력
maze = [list(map(int,input())) for _ in range(n)] #미로 입력 
def bfs(): #bfs 로 구현
    queue=deque() #좌표와 찬스를 기록할 큐
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)] #방문한 값을 저장할 리스트
                                                            #벽뿌수기 찬스 유무 구별을 위해 3차원배열로 선언
    
    dx, dy = [-1,1,0,0],[0,0,-1,1] #x,y 이동하는 경우의 수
    visited[0][0][True] = 1 #문제 조건에 맞게 첫번째 방문 카운트
    queue.append([0,0,True]) #0,0 찬스(ㅇ) 큐에 삽입
    while queue: #큐가 빌때까지 반복
        x,y,chance = queue.popleft() #선입선출 빼주기
        if x==n-1 and y==m-1: #x,y가 (n,m)행렬의 마지막 좌표라면
            return visited[x][y][chance] #함수 종료 후 마지막 좌표값 반환
                                         #bfs 라면 가장 먼저 도착한 값이 최소값일테니까
                                
        for i in range(4):#상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m: #리스트(행렬) 인덱스 범위안에 들어가야하므로    
                if chance and maze[nx][ny]: #찬스가 있고 미로가 벽이라면
                    visited[nx][ny][False]=visited[x][y][True]+1 #찬스(x) 리스트에 이전 이동값+1
                    queue.append([nx,ny,False]) #찬스 없애고 append
                elif not maze[nx][ny] and not visited[nx][ny][chance]: #인덱스 안에서 벽이 없는 공간으로 움직일 때
                    visited[nx][ny][chance]=visited[x][y][chance]+1
                    queue.append([nx,ny,chance])
    return -1 #큐가 빌때까지 반복을 했지만 마지막 좌표값 반환을 하지 못했을 때
              #마지막 좌표값을 반환하지 못했다는 것은 목적지에 도착하지 못했다는 뜻

print(bfs())