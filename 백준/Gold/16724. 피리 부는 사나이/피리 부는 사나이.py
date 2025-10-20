import sys

# 1. 입력 받기
input = sys.stdin.readline

n,m = map(int, input().split())
lst = [list(input().strip()) for _ in range(n)]
state = [[0]*m for _ in range(n)] #0:방문전/1:사이클진행중/2:사이클완료

dic = {}
dic['U'] = (-1,0)
dic['D'] = (1,0)
dic['L'] = (0,-1)
dic['R'] = (0,1)

def dfs(r,c):
    global ans
    state[r][c] = 1 #지금 현 dfs에서 사이클 찾기 진행중
    dr,dc = dic[lst[r][c]]
    nr,nc = r+dr, c+dc

    if state[nr][nc] == 0: # 아직 방문x
        dfs(nr,nc) #dfs 계속
    elif state[nr][nc] == 1: #이번 턴에서 사이클 발견!
        ans += 1

    state[r][c] = 2 #사이클 발견 or 있던 사이클에 탑승하면, 그 노드는 완료표시! 그리고 되돌아가며 그턴에 포함된 애들도 완료 표시됨!


ans = 0
for i in range(n):
    for j in range(m):
        if state[i][j] == 0: #아직 방문x
            dfs(i,j)

print(ans)

