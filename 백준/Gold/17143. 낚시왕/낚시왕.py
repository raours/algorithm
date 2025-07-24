'''
2025.7.23
백준 : 낚시왕
'''
import sys
input = sys.stdin.readline

r,c,m = map(int, input().split())
shark = []
for i in range(m):
  rr, cc, s, d, z = map(int, input().split())
  shark.append((rr-1,cc-1,s,d-1,z))

dr = [-1,1,0,0] #위아래오른왼
dc = [0,0,1,-1]

def move_shark(rr,cc,s,d):
    global r, c
    if d in [0,1]: #위아래 움직임
        size = 2* (r-1)
        s = s%size
        for _ in range(s):
            if rr == 0 and d == 0: #위의 벽, 방향 위일 때
                d = 1 #방향 아래로 전환
            elif rr == r-1 and d == 1:
                d = 0 #방향 위로 전환
            rr += dr[d]

    else: #좌우
        size = 2* (c-1)
        s = s%size
        for _ in range(s):
            if cc == 0 and d == 3: #왼쪽 벽, 방향 왼일 때
                d = 2 #방향 오른로 전환
            elif cc == c-1 and d == 2:
                d = 3 #방향 왼쪽으로 전환
            cc += dc[d]
    return rr,cc,d


ans = 0
for t in range(c): #6초동안!
    up = 1000000000
    shark_idx = -1
    for idx in range(len(shark)):
        #1. 낚시왕이 상어를 잡을 수 있는지 확인
        # shark 리스트를 돌며, 그 열 중에 가장 위에 있는 상어의 인덱스 저장
        # 다 돌았으면, 찾은 인덱스로 상어 잡기 // 없으면 패스
        rr, cc, s, d, z = shark[idx]
        if cc == t:
           if up>rr:
              shark_idx = idx
              up = rr
    
    if shark_idx>-1:
       ans += shark[shark_idx][4]
       shark[shark_idx] = -1,-1,-1,-1,-1 #상어 잡음!

    #2. 남은 상어들의 움직임 start
    # 상어리스트를 돌며, 이동시키는데 칸수만큼 움직이되 벽을 마주치면, 방향 바꿔서 계속 이동
    board = [[[] for _ in range(c)] for _ in range(r)]
    for idx in range(len(shark)):
        rr, cc, s, d, z = shark[idx]
        if (rr,cc) == (-1,-1): #잡힌 상어는 pass
            continue
        #상어 s칸 만큼 움직임!
        rr,cc,d= move_shark(rr,cc,s,d)

        shark[idx] = (rr, cc, s, d, z) 
        # 그리고 도착한 칸에 대해 board에 상어 인덱스와 크기... 놓기?       
        board[rr][cc].append((z, idx))
    
    #3. 다 끝나면, board를 순회하며, shark가 중복으로 되어 있는 곳에 크기가 제일 큰 상어 빼고,
    # 다 잡아먹힘!
    for i in range(r):
        for j in range(c):
            if len(board[i][j]) > 1: #상어 여러마리면
                board[i][j].sort()
                for kk in range(len(board[i][j])-1):
                    shark[board[i][j][kk][1]] = (-1,-1,-1,-1,-1)

print(ans)    
                 