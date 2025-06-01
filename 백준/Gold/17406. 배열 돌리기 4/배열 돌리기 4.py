from itertools import permutations
import sys

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
rot = [list(map(int, input().split())) for _ in range(K)]

c = [i for i in range(K)]
answer = 5001

dr = 0,1,0,-1 #우하좌상
dc = 1,0,-1,0
for permu in permutations(c, K):
    lst2 = [arr[:] for arr in lst]
    for i in permu:
        #회전시키고
        r,c,s = rot[i]
        #바깥부터 안쪽으로 시계방향 회전 각각 진행
        for j in range(s): #각 테두리 범위를 만들 j변수
            top_r,top_c = r-s+j-1, c-s+j-1
            bottom_r,bottom_c = r+s-j-1, c+s-j-1

            y,x = top_r,top_c #시작점
            prev = lst2[y][x]

            for d in range(4): #우하좌상 각각 방향으로 쫙 해보고 다음 방향으로!
                while True:
                    ny,nx = y+dr[d],x+dc[d]
                    if not(top_r<=ny<=bottom_r and top_c<=nx<=bottom_c):
                        break # 움직인 곳이 범위내x
                    #이동시키기
                    lst2[ny][nx], prev = prev, lst2[ny][nx]
                    y,x = ny,nx #옮길 좌표 갱신

    # 배열 값 구하기
    temp = 5001
    for i in range(N):
        temp = min(temp, sum(lst2[i]))
    answer = min(answer,temp)
print(answer)



