'''
2025.8.28
'''
import sys
input = sys.stdin.readline


lst = [list(map(int, input().split())) for _ in range(5)]

dr = [0,-1,0,1]
dc = [-1,0,1,0]

def dfs(cr,cc,temp):
    temp += str(lst[cr][cc]) #새로운 문자열 생성
    if len(temp)==6:
        ans.add(temp)
        return #이때 돌아가면 바깥 함수는 전의 temp를 사용중 -> 자동 백트래킹 효과

    for k in range(4):
        nr, nc = cr+dr[k], cc+dc[k]
        if 0<=nr<5 and 0<=nc<5:
            dfs(nr,nc,temp)
    return


ans = set()
for i in range(5):
    for j in range(5):
        dfs(i,j, '')

print(len(ans))