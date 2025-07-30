'''
2025.7.29-7.31
백준 : 감시
'''
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
cctv = []
for i in range(n):
    temp = list(map(int,input().split()))
    lst.append(temp)
    for j in range(m):
        if temp[j] > 0 and temp[j] != 6: # cctv이면,
            cctv.append([temp[j],i,j]) #번호, 좌표, 방향

#cctv 번호별 가능한 방향
mode = [
    [], [[0],[1],[2],[3]], [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]], [[0,1,2],[0,1,3],[0,2,3], [1,2,3]],
    [[0,1,2,3]]
]
dr = [0,1,0,-1] #동, 남,서,북
dc = [1,0,-1,0]

def fill(temp, num, x,y):
    for i in num: #예시 [0,2]
        #저 방향으로 cctv 모두 check
        nx, ny = x,y
        while True:
            nx, ny = nx+dr[i], ny+dc[i]
            if 0>nx or nx >= n or 0>ny or ny>= m: #범위 밖이면,
                break # 즉시 중단
            if temp[nx][ny] == 6: #벽이면 중단
                break
            if temp[nx][ny] == 0: #빈칸이면, cctv 가능
                temp[nx][ny] = -1



ans = 1e9
#dfs로 cctv 다 회전 시켜보기
def dfs(depth, lst): #어디까지 탐색했으며, 지금 lst의 상태 넘기기
    global ans
    if depth == len(cctv): # 모든 cctv에 대해 돌았으면,
        cnt = 0
        #사각지대 계산
        for i in range(n):
            cnt += lst[i].count(0)
        ans = min(ans, cnt)
        return

    # 이전 값 복제 : cctv를 정하고, 사각지대를 구할 것이므로,
    temp = [arr[:] for arr in lst]
    cctv_num, x,y = cctv[depth] # depth번째 cctv 정보를 꺼내서
    for i in mode[cctv_num]: #번호마다 방향 경우의 수가 여러개인데 그걸 하나씩
        #그 번호에 맞는 방향  숫자가 들어가있는 lst를 넘겨받음
        fill(temp, i, x,y) #현재좌표, 그 번호의 방향 리스트 넘버, lst복사좌표
        dfs(depth+1, temp)
        #다음 방향 숫자 리스트 돌리기 전에, temp 를 원래 데이터로 복귀
        temp = [arr[:] for arr in lst]



dfs(0,lst)
print(ans)