'''
2025.7.1-7.2
백준 : 벽 부수고 이동하기 4
'''
from collections import deque
import sys

n, m = map(int, input().split())

lst = [list(map(int, input().strip())) for _ in range(n)]


cnt = [] #0의 개수를 저장해놓는 배열

visit = [[0]*m for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]

dic = {}
#0으로 연결된 부분을 숫자로 visit에 표기하기(1부터)
def bfs(r,c,index):
    q = deque()
    q.append((r,c))
    visit[r][c] = index
    cnt = 1

    while q: #시작점에서 갈 수 있는 곳을 bfs 돌며 모두 index로 채우기
        cr, cc = q.popleft()
        for i in range(4):
            nr, nc = cr+dr[i], cc+dc[i]
            if 0<=nr<n and 0<=nc<m and lst[nr][nc] == 0 and visit[nr][nc] == 0:
                q.append((nr,nc))
                visit[nr][nc] = index
                cnt += 1
    dic[index] = cnt

    return
    

index = 10
for i in range(n):
    for j in range(m): #lst를 모두 돌며, 0의 정보를 추출하자
        if lst[i][j] == 0 and visit[i][j] == 0: #벽x, 방문x
            bfs(i, j, index)
            index += 1

# for i in range(len(visit)):
#     print(visit[i])
# print(dic)

answer = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1: #벽이면 계산하자!
            temp = 0
            visited = set() #중복 그룹 여부 확인! list보단 set을 쓰자! list에서의 in: O(n) vs set에서의 in: O(1)
            for k in range(4):
                ni,nj = i+dr[k],j+dc[k]
                if 0<=ni<n and 0<=nj<m and visit[ni][nj]>=10:
                    #범위내, 계산된 이동할 수 있는 칸들이 있으면,
                    group = visit[ni][nj]
                    if not group in visited:
                        temp += (dic[group]) #미리 계산해놓은 합산 값을 더해주기
                        visited.add(group)
            answer[i][j] = (temp+1)%10 #+자기자신(1)

#출력 형식! ''.join 기억하기
for row in answer:
    print(''.join(map(str, row)))


