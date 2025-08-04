import sys  
from collections import defaultdict  


N, M, K = map(int, input().split())  
arr = [[[] for _ in range(N)] for _ in range(N)]  
fireball = []  
# 방향  
di, dj = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  

for _ in range(M):  
    r, c, m, s, d = map(int, input().split())  
    fireball.append((r-1, c-1, m,s,d))  

for _ in range(K):  
    while fireball:  
        cr, cc, cm, cs, cd = fireball.pop()  
        # 1번과 N번이 연결되어 있으므로 %로 나눠준다.  
        nr = (cr + cs * di[cd]) % N  
        nc = (cc + cs * dj[cd]) % N  
        arr[nr][nc].append([cm, cs, cd])  

    # 2개 이상인지 체크  
    for r in range(N):  
        for c in range(N):  
            if len(arr[r][c]) >= 2:  
                # 4개로 쪼개기  
                val_m, val_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(arr[r][c])  
                while arr[r][c]:  
                    m, s, d = arr[r][c].pop()  
                    val_m += m  
                    val_s += s  
                    if d % 2:  
                        cnt_odd += 1  
                    else:  
                        cnt_even += 1  
                if cnt_odd == cnt or cnt_even == cnt:  
                    nd = [0, 2, 4, 6]  
                else:  
                    nd = [1, 3, 5, 7]  

                if val_m // 5:  
                    for i in nd:  
                        fireball.append([r, c, val_m//5, val_s//cnt, i])  

            elif len(arr[r][c]) == 1:  
                fireball.append([r, c] + arr[r][c].pop())  

print(sum(i[2] for i in fireball))