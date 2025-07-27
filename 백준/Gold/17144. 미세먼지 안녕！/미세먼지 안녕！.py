'''
2025.7.25, 7.27
백준 : 미세먼지 안녕!
'''
import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
lst = []
robot = []
for i in range(r):
    temp = list(map(int,input().split())) 
    lst.append(temp)
    for j in range(c):
        if temp[j] == -1:
            robot.append((i,j))
            

dr = [1,-1,0,0]
dc = [0,0,1,-1]
for T in range(t):
    #미세먼지 확산
    #모든 칸을 돌며, 미세먼지가 있으면 확산, 
    spread = [[0]*c for _ in range(r)] #여기에 확산된 정보 저장
    for i in range(r) :
        for j in range(c):
            if lst[i][j] > 0:
                a = lst[i][j]
                plus = a//5
                cnt = 0
                for k in range(4):
                    nr, nc = i+dr[k], j+dc[k]
                    if 0<=nr<r and 0<=nc<c and lst[nr][nc] >= 0:
                        spread[nr][nc] += plus
                        cnt += 1 #확산된 개수 + 1

                spread[i][j] += (lst[i][j]-plus*cnt)
    
    # for i in range(r):
    #     print(*spread[i])

    #공기청정기 작동! 항상 1열에 위치하고 있음
    # 위 공기 청정기 robot[0]
    ur, uc = robot[0]
    downr, downc = robot[1]
    #소멸
    if spread[ur-1][uc] > 0:
        spread[ur-1][uc] = 0
    # 아래
    for i in range(ur-1, 0, -1): #한칸씩 끌어내리기
        if spread[i-1][uc] >0:
            spread[i][uc] = spread[i-1][uc]
            spread[i-1][uc] = 0

    #맨 윗줄 왼쪽으로 한칸씩 이동
    for i in range(c-1):
        if spread[0][i+1] > 0:
            spread[0][i] = spread[0][i+1]
            spread[0][i+1] = 0

    #위로 한칸씩 이동
    for i in range(ur):
        spread[i][c-1] = spread[i+1][c-1]
        spread[i+1][c-1] = 0
    
    #오른쪽으로 이동
    for i in range(c-1, uc, -1):
        spread[ur][i] = spread[ur][i-1]
        spread[ur][i-1] = 0
    
    
    #공기청정기 아래부분 start
    #위로 한칸씩 이동
    for i in range(downr+1, r-1):
        spread[i][0] = spread[i+1][0]
        spread[i+1][0] = 0

    #왼쪽으로 한칸씩 이동
    for i in range(c-1):
        if spread[r-1][i+1] > 0:
            spread[r-1][i] = spread[r-1][i+1]
            spread[r-1][i+1] = 0 
    
    # 아래
    for i in range(r-1, downr, -1): #한칸씩 끌어내리기
        if spread[i-1][c-1] >0:
            spread[i][c-1] = spread[i-1][c-1]
            spread[i-1][c-1] = 0

    #오른쪽으로 이동
    for i in range(c-1, downc+1, -1):
        spread[downr][i] = spread[downr][i-1]
        spread[downr][i-1] = 0

    #로봇 자리 다시 표시
    spread[ur][uc] = -1
    spread[downr][downc] = -1

    # for i in range(r):
    #     print(spread[i])
    
    lst = spread

   

#답 구하기
ans = 0
for i in range(r):
    for j in range(c):
        if lst[i][j]>0:
            ans += lst[i][j]

print(ans)

