from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    lst = [[-1] * 102 for _ in range(102)]
    
    #테투리는 1, 직사각형 내부는 0 으로 채우기
    for rect in rectangle:
        x1,y1,x2,y2 = map(lambda x: x*2, rect)
        for i in range(x1,x2+1): #하나의 점이 하나의 칸이 되므로-> 범위는 x1두배 좌표~x2 두배 좌표가 맞음!
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2: #내부는 0으로 덮고
                    lst[i][j] = 0
                elif lst[i][j] != 0:  #다른 직사각형의 내부가 아닌 곳만 테두리로!  
                    lst[i][j] = 1
                    
    #BFS로 최단경로 찾기! 찾고나서 나누기 2해줘야함!
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    visit = [[False] * 102 for _ in range(102)]
    visit[characterX*2][characterY*2] = True
    
    while q:
        cx,cy,d = q.popleft()
        
        if (cx,cy) == (itemX*2, itemY*2):
            answer = d//2
            break
        for dx,dy in ((1,0),(-1,0),(0,-1),(0,1)):
            nx,ny = cx+dx,cy+dy
            if 0<=nx<102 and 0<=ny<102 and not visit[nx][ny] and lst[nx][ny] == 1:
                q.append((nx,ny,d+1))
                visit[nx][ny] = True
        
            
            
    return answer