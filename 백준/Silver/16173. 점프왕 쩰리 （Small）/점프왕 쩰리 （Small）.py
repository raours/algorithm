'''
2025.8.26
'''
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dr = [0,1]
dc = [1,0]

def dfs(r,c):
    visit[r][c] = 0

    step = board[r][c] #갈 수 있는 칸 수
    if step == 0: return
    for i in range(2):
        nr,nc = r+dr[i]*step, c+dc[i]*step #다음 칸
        if 0<=nr<n and 0<=nc<n and visit[nr][nc] == 0:
            if (nr, nc) == (n - 1, n - 1):  # 도착
                print("HaruHaru")
                exit()
            dfs(nr,nc)
    return 

visit = [[0]*n for _ in range(n)]
dfs(0,0)

print('Hing')
