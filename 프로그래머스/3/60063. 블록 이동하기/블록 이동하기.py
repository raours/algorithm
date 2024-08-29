from collections import deque

def get_np(pos, nboard): #갈 수 있는 다음 위치를 모두 리스트에 담아 찾아 넘겨줌
    np =[]
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    #상하좌우 이동
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx1, ny1, nx2, ny2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
        #비어있어야 이동 가능
        if nboard[nx1][ny1] ==0 and nboard[nx2][ny2] ==0:
            np.append({(nx1, ny1),(nx2,ny2)}) 
    if x1 == x2: 
        #가로로 놓여있으면 위아래로 회전 가능
        for i in [-1, 1]:
            nx1, nx2= x1+i, x2+i
            #위아래가 비어있으면
            if nboard[nx1][y1] ==0 and nboard[nx2][y2] ==0:
                np.append({(x1, y1),(nx1,y1)}) 
                np.append({(nx2, y2),(x2,y2)})
    elif y1 == y2:
        #세로로 놓여있으면 오른쪽, 왼쪽으로 회전 가능
        for i in [-1, 1]:
            #오른쪽, 왼쪽이 비어있으면
            if nboard[x1][y1+i] ==0 and nboard[x2][y2+i] ==0:
                np.append({(x1, y1),(x1,y1+i)}) 
                np.append({(x2, y2),(x2,y2+i)})
    return np
                
            
    


def solution(board):
    n = len(board)
    nboard = [[1] *(n+2) for _ in range(n+2)]
    for i in range(n): #board를 벽으로 감싸기
        for j in range(n):
            nboard[i+1][j+1] = board[i][j]
    
    q = deque()
    p = {(1,1), (1,2)} #첫 위치
    
    visited = []
    q.append((p,0)) #초기값 설정
    visited.append(p)
    
    #BFS 최단거리
    while q:
        pos, t = q.popleft()
        #(n,n)에 도달했다면 그 시간 return
        if (n,n) in pos:
            return t
        
        for np in get_np(pos, nboard):
            if np not in visited:
                #방문한 적이 없으면
                q.append((np, t+1))
                visited.append(np)
                
    
    
    
    
  