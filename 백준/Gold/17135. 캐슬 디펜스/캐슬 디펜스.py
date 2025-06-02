from itertools import combinations
import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
for a,b,c in combinations(range(M),3):
    ans = 0
    lst = [arr[:] for arr in board]
    #한 사이클 시작
    while True:
        #적이 모두 없어지면 종료
        flag = True
        for i in range(N):
            for j in range(M):
                if lst[i][j] == 1:
                    flag = False
        if flag == True:
            break

        #궁수 공격
        temp1,temp2,temp3 = 1e9,1e9,1e9
        for j in range(M): #왼쪽 우선
            for i in range(N): #모든 칸을 돌며 적과의 거리 확인
                if lst[i][j] == 1:
                    if abs(i-N)+abs(j-a)<=D and temp1 > abs(i-N)+abs(j-a):
                        ar,ac = i,j
                        temp1 = abs(i-N)+abs(j-a)

                    if abs(i-N)+abs(j-b)<=D and temp2 > abs(i - N) + abs(j - b):
                        br, bc = i, j
                        temp2 = abs(i - N) + abs(j - b)

                    if abs(i-N)+abs(j-c)<=D and temp3 > abs(i-N)+abs(j-c):
                        cr,cc = i,j
                        temp3 = abs(i-N)+abs(j-c)

        if temp1 < 1e9:
            lst[ar][ac] = 0
            ans += 1

        if temp2 < 1e9:
            if lst[br][bc] != 0:
                lst[br][bc] = 0
                ans += 1

        if temp3 < 1e9:
            if lst[cr][cc] != 0:
                lst[cr][cc] = 0
                ans += 1

        # 적 이동
        for i in range(N-1,-1,-1):
            for j in range(M):
                if lst[i][j] == 1: #그 자리에 적o
                    if 0<=i+1<N:
                        lst[i+1][j] = 1
                        lst[i][j] = 0
                    elif i+1 == N: #성에 도착
                        lst[i][j] = 0


    result = max(result, ans)
print(result)