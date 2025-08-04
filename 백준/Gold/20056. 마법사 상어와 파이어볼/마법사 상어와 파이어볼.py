'''
2025.8.4
백준 : 마법사 상어와 파이어볼
'''
import sys

input = sys.stdin.readline

n,m,k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]

fire = []
for i in range(m):
    r,c,m,s,d = map(int, input().split())
    fire.append((r-1,c-1,m,s,d))


dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]


for turn in range(k): #k번 반복
    #모든 파이어볼 이동
    board = [[[] for _ in range(n)] for _ in range(n)]

    for f in range(len(fire)):
        r, c, m, s, d = fire[f]
        if (r,c) == (-1,-1): # 합쳐진 파이어볼
            continue
        nr, nc = (r + dr[d] * s) % n, (c + dc[d] * s) % n
        fire[f] = (nr, nc, m, s, d)
        board[nr][nc].append(f)

    # 파이어 볼 합치기
    for i in range(n):
        for j in range(n):
            if len(board[i][j])>1: # 2개이상 있으면,
                new_m, new_s = 0,0
                new_d = []
                a = board[i][j]
                for ff in range(len(a)):
                    temp_r, temp_c, temp_m, temp_s, temp_d = fire[a[ff]]
                    fire[a[ff]] = (-1,-1,-1,-1,-1) #합쳐진 애 표시
                    new_d.append(temp_d)
                    new_s += temp_s
                    new_m += temp_m

                new_m = new_m // 5
                new_s = new_s // len(a)

                if new_m == 0: #질량 0이면 소멸!
                    continue

                # all(조건 for 원소 in list) 모든 원소가 조건 만족하는지 검사
                all_even = all(dd % 2 == 0 for dd in new_d)
                all_odd = all(dd % 2 != 0 for dd in new_d)

                if all_even or all_odd: #모두 짝수거나 모두 홀수면
                    final_d = [0,2,4,6]
                else:
                    final_d = [1, 3, 5, 7]

                #새로 나누어진 파이어볼 정보 저장
                for fd in final_d:
                    fire.append((i,j,new_m, new_s, fd))


#남아있는 파이어볼 질량의 합 구하기
ans = 0
for i in range(len(fire)):
    if fire[i][0] == -1: #합쳐진 애면 pass
        continue
    ans += fire[i][2]
print(ans)


