'''
2025.9.7
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = [list(map(int, input().strip())) for _ in range(n)]

ans = []
def solve(s,r,l):
    num = lst[s][r] #시작점 숫자가 기준

    for i in range(s,s+l):
        for j in range(r,r+l):
            if lst[i][j] != num:
                print('(', end='')
                solve(s,r,l//2)
                solve(s, r+l//2, l//2)
                solve(s+l//2, r, l//2)
                solve(s+l//2, r+l//2, l//2)
                print(')', end ='')
                return

    print(num, end = '')

solve(0,0,n)
