'''
2025.9.3
'''
import sys
from collections import deque

n, m = map(int, input().split())
lst = [list(map(str, input().strip())) for _ in range(n)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(i,j,start):
    temp = 0
    # # 시작, W일때
    # bfs(i, j, 'W')

    visit = [[None] * m for _ in range(n)]  # 방문 체크

    if start == 'W':
        if lst[i][j] == 'B':
            temp += 1  # 변경
        visit[i][j] = 'W'  # 체크

    if start == 'B':
        if lst[i][j] == 'W':
            temp += 1  # 변경
        visit[i][j] = 'B'  # 체크

    q = deque()
    q.append((i, j))

    while q:
        sr, sc = q.popleft()

        for k in range(4):
            nr, nc = sr + dr[k], sc + dc[k]

            if i <= nr < i + 8 and j <= nc < j + 8 and not visit[nr][nc]:
                if visit[sr][sc] == lst[nr][nc]:  # 인접한 부분이 같으면, 변경
                    temp += 1

                # 방문처리 및 정보저장
                if visit[sr][sc] == 'W':
                    visit[nr][nc] = 'B'
                else:
                    visit[nr][nc] = 'W'
                q.append((nr, nc))  # 큐에 삽입
    return temp

ans = 1e9
for i in range(n-7): #시작점 고르기
    for j in range(m-7):
        #시작, W일때
        ans = min(ans, bfs(i,j,'W'))

        #시작, B일때
        ans = min(ans, bfs(i,j,'B'))

print(ans)
