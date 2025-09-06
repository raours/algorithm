'''
2025.9.7
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

ans = [0,0,0]
def solve(s,r,l):
    num = lst[s][r] #시작점 숫자가 기준

    for i in range(s,s+l):
        for j in range(r,r+l):
            if lst[i][j] != num:
                solve(s,r,l//3)
                solve(s, r+l//3, l//3)
                solve(s, r+l*2//3, l//3)

                solve(s+l//3, r, l//3)
                solve(s+l//3, r+l//3, l//3)
                solve(s+l//3, r+l*2//3, l//3)

                solve(s + l*2 // 3, r, l // 3)
                solve(s + l*2 // 3, r + l // 3, l // 3)
                solve(s + l*2 // 3, r + l * 2 // 3, l // 3)

                return

    if num == -1:
        ans[0] += 1
    elif num == 0:
        ans[1] += 1
    else:
        ans[2] += 1


solve(0,0,n)
print(*ans, sep = '\n')