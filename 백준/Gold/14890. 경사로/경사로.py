'''
2025.7.20
백준 : 경사로
'''
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


ans = 0
#가로 줄 먼저
for i in range(n):
    # chk = lst[]
    flag = True #길인지 아닌지
    next_dup = 0
    j = 0
    sliding = [False]*n #경사로 놓였는지 아닌지
    while True:
        if j >= n-1: #끝에 도달하면, 종료
            break

        if lst[i][j] == lst[i][j+1]: #다음 애랑 같으면,
            j += 1
        elif lst[i][j] == lst[i][j+1]+1: #다음이 1칸 낮으면
            #이후, 낮은 칸이 L칸 지속되는지 확인해야함
            yes = True
            a = lst[i][j+1]
            for k in range(j+1, j+1+l):
                if k>n-1 or lst[i][k] != a:
                    yes = False
                    break
                sliding[k] = True

            if not yes: #경사로 못 놓으면 길 x
                flag = False
                break
            # 경사로 놓을 수 있으면,
            # 그 다음 칸,
            j = j+l


        elif lst[i][j]+1 == lst[i][j + 1]:  # 다음이 1칸 높으면
            #이전의 L칸이 한칸 낮은지 확인
            yes = True
            b = lst[i][j]
            for k in range(j-l+1, j+1):
                if k<0 or sliding[k] or lst[i][k] != b:
                    yes = False
                    break
                sliding[k] = True
                #그 j자리도 sliding true해줘야함

            if not yes:  # 경사로 못 놓으면 길 x
                flag = False
                break
            # 경사로 놓을 수 있으면,
            sliding[j] = True
            j += 1



        else: #그 이외는 길 못 만드니까 break
            flag = False
            break

    if flag: #길이면,
        ans += 1

# 세로 줄
for i in range(n):
    # chk = lst[]
    flag = True  # 길인지 아닌지
    next_dup = 0
    j = 0
    sliding = [False] * n  # 경사로 놓였는지 아닌지
    while True:
        if j >= n - 1:  # 끝에 도달하면, 종료
            break

        if lst[j][i] == lst[j+1][i]:  # 다음 애랑 같으면,
            j += 1
        elif lst[j][i] == lst[j+1][i] + 1:  # 다음이 1칸 낮으면
            # 이후, 낮은 칸이 L칸 지속되는지 확인해야함
            yes = True
            a = lst[j+1][i]
            for k in range(j + 1, j + 1 + l):
                if k>n-1 or lst[k][i] != a:
                    yes = False
                    break
                sliding[k] = True


            if not yes:  # 경사로 못 놓으면 길 x
                flag = False
                break
            # 경사로 놓을 수 있으면,

            j = j + l

        elif lst[j][i] == lst[j+1][i] - 1:  # 다음이 1칸 높으면
            # 이전의 L칸이 한칸 낮은지 확인
            yes = True
            b = lst[j][i]
            for k in range(j - l + 1, j+1):
                if k<0 or sliding[k] or lst[k][i] != b:
                    yes = False
                    break
                sliding[k] = True

            if not yes:  # 경사로 못 놓으면 길 x
                flag = False
                break
            # 경사로 놓을 수 있으면,
            sliding[j] = True
            j += 1

        else:  # 그 이외는 길 못 만드니까 break
            flag = False
            break

    if flag:  # 길이면,
        ans += 1
print(ans)