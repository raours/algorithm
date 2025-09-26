'''
2025.9.26
'''
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input().strip())
lst = [list(map(int, input().split())) for _ in range(n)]

# 거리테이블로 변경
for i in range(n):
    for j in range(n):
        if lst[i][j] == 0: #문제 조건 상 i->i 는 길없다함
            lst[i][j] = INF

#갈 수 있는 경로 모두 체크 : 플로이드 워셜로!
for k in range(n):
    for i in range(n):
        for j in range(n):
            lst[i][j] = min(lst[i][j], lst[i][k]+lst[k][j])

for i in range(n):
    for j in range(n):
        if lst[i][j] == INF:
            lst[i][j] = 0
        
        else:
            lst[i][j] = 1
for a in lst:
    print(*a)