'''
2025.9.7
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
def solve(s,r,size):
    global white, blue
    color = lst[s][r] #시작점 색깔!
    for i in range(s, s+size):
        for j in range(r,r+size):
            if lst[i][j] != color: #시작점과 색깔이 같지 않다면, 색종이 잘라야함
                #4조각으로 자른 색종이에 대해 재귀함수!
                #재귀함수 기준은 현재 바깥 함수의 시작점(s,r)!을 기준으로 4조각임
                solve(s,r,size//2) #왼쪽 위
                solve(s+size//2,r,size//2) #왼쪽 아래
                solve(s,r+size//2,size//2) #오른쪽 위
                solve(s+size//2,r+size//2,size//2) #오른쪽 아래

                return

    #나눠진 조각 안이이 모두같은 색깔!
    if color == 0:
        white += 1
    else:
        blue += 1

solve(0,0,n)
print(white)
print(blue)

