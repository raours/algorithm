'''
2025.7.20
백준 : 사다리 조작
'''
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
lst = [[False]*(n) for _ in range(h)]
for _ in range(m):
    a,b = map(int, input().split()) #가로, 세로
    lst[a-1][b-1] = True

def chk():
    for i in range(n): #각 인덱스에 대해 사다리 타보기
        start = i
        r, c = 0, i
        while r <= h-1:
            #연결된 오른쪽 가로선이 있다면,
            if lst[r][c]:
                c += 1
            #왼쪽 가로선이 있다면,
            elif c-1>=0 and lst[r][c-1]:
                c -= 1
            r += 1

        if c != start:  # i번째가 i번 지점에 도착x
            return False

    return True # 정답이면 return True


#사다리를 어떻게 설치할 것인가..?
# DFS+백트래킹
def dfs(cnt, x, y):
    global ans
    #백트래킹 return 조건
    if chk(): #성공
        ans = min(ans, cnt) #최솟값으로 갱신
        return
    if cnt >= 3 or ans <= cnt:
        return #더이상 사다리 설치 의미 x


    for r in range(x, h): #행의 범위
        if r == x: #탐색하던 행이면,
            now = y #탐색하던 열부터 시작하고
        else: #다른 행이면, 열번호 0부터!
            now = 0
        for c in range(now, n-1):
            #설치 가능한지 확인
            if lst[r][c] == False and lst[r][c+1] == False: #오른쪽 두칸 확인
                if c>=0 and lst[r][c-1] == False: #왼쪽 확인
                    lst[r][c] = True #사다리 설치
                    dfs(cnt+1, r, c+2)  # 설치한 열의 +2부터 봐야함! 나란히 설치 안되므로!
                    lst[r][c] = False #사다리 치우기


ans = 4 #최대 값
dfs(0,0,0) #몇개를 설치했는가/ 행/ 열

if ans > 3:
    print(-1)
else:
    print(ans)