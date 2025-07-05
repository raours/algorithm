'''
2025.07.02-07.03, 7/5
백준 : 로봇 청소기
'''
import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if (w,h) == (0,0):
        break
    lst = [list(map(str, input().strip())) for _ in range(h)]

    board = [[0]*w for _ in range(h)]
    dirty = []
    #문자별 정보 저장, 더러운 칸 총 몇개인지 계산
    cnt = 0
    # index = 1
    for i in range(h):
        for j in range(w):
            if lst[i][j] == '*': #더러운 칸
                # board[i][j] = index
                # index += 1
                dirty.append((i,j))
                cnt += 1
            elif lst[i][j] == 'x': #가구
                board[i][j] = -1

            elif lst[i][j] == 'o': #로봇 청소기
                x,y = i,j


    dr = [0,0,-1,1]
    dc = [1,-1,0,0]

    def bfs(r,c): #(r,c)로부터의 거리가 저장된 visited 배열 구하기!
        q = deque()
        q.append((r,c))
        visited = [[0]*w for _ in range(h)]
        visited[r][c] = 1

        while q:
            rr,cc = q.popleft()
            for i in range(4):
                nr,nc = rr+dr[i],cc+dc[i]
                if 0<=nr<h and 0<=nc<w and board[nr][nc] >=0 and visited[nr][nc] == 0:
                    q.append((nr,nc)) 
                    visited[nr][nc] = visited[rr][cc]+1
        
        return visited
        

    #1. 처음 청소기 위치에서 먼지들과의 거리 구하기 
    # (청소기 위치에서 bfs 다 돌려서 visited 배열에 거리 저장해놓으면 한번에 구할 수 있다!)
    temp = bfs(x,y)


    #먼지들끼리의 거리 구해서 2차원 배열에 넣기
    dirty_dis = [[0]*cnt for _ in range(cnt)]

    for i in range(cnt):
        a,b = dirty[i] #i번째 먼지 위치
        #여기서 로봇 청소기가 먼지까지 못 가는 경우면 바로 -1출력
        temp2 = bfs(a,b) #그 먼지에서의 bfs함수 거쳐 visited 맵 탐색
        for j in range(cnt):
            aa,bb = dirty[j]
            dirty_dis[i][j] = temp2[aa][bb]-1 #i번째 먼지->j번째 먼지로의 이동 거리!


    answer = []
    #순열을 이용해서 먼지를 탐색할 순서를 정하고 완탐!
    for idx_list in permutations(range(cnt),cnt): #순열로 구한 순서들의 list #(0,1,2), (0,2,1) ,,, 
        d = 0
        #로봇 -> 첫 먼지 (인덱스값 : idx_list[0] )
        flag2 = False
        x1,y1 = dirty[idx_list[0]] #idx_list = (0,1,2)
        if temp[x1][y1] == 0: #도달하지 못하는 것이므로, answer = -1
            flag2 = True
            break

        d += (temp[x1][y1]-1)
        flag = True
        #먼지 -> 먼지
        for i in range(len(idx_list)-1):
            if dirty_dis[idx_list[i]][idx_list[i+1]] == 0: #먼지에서 먼지로 못가면 그 경로는 out
                flag = False
                break
            d += (dirty_dis[idx_list[i]][idx_list[i+1]])
        
        if flag == False:
            continue
        answer.append(d)

    if len(answer)>0 and flag2 == False:
        print(min(answer))
    else : print(-1)
        


