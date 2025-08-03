'''
2025.8.3
백준 : 게리맨더링
'''
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n = int(input())
cnt = list(map(int, input().split()))

lst = [[]]
for _ in range(n):
    temp = list(map(int, input().split()))
    lst.append(temp[1:])

def bfs(area):
    start = area[0]
    visit = [0] * (n+1)
    q = deque()
    q.append((start))
    visit[start] = 1 
    human_cnt = cnt[start-1] # 시작한 자치구의 인구수
    visit_cnt = 1 #시작한 자치구 1개!
    while q:
        current = q.popleft()
        for i in lst[current]:
            if visit[i] == 0 and i in area: #방문한적 x , 조합으로 나눠놓은 자치구에 있으면,
                q.append(i)
                visit[i] = 1
                human_cnt += (cnt[i-1])
                visit_cnt += 1
    return visit_cnt, human_cnt



#선거구 조합으로 나누기 (1~n//2까지만 하면 됨!)
a = [b for b in range(1,n+1)]
ans = 1e10
for j in range(1, n//2+1):
    for combi in combinations(a,j):
        #나눠진 선거구 리스트를 bfs로 다 연결되어 있는지 확인
        #인구수 확인
        num1, human1 = bfs(combi)
        if num1 != len(combi):
            continue
        #나머지 선거구에 대해서도 bfs 다 연결되어 있는지 확인, 인구수 확인
        not_combi = [x for x in range(1,n+1) if x not in combi]
        #가능한 경우면, 인구수 차이 update
        num2, human2 = bfs(not_combi)
        if num2 != len(not_combi):
            continue
        ans = min(ans, abs(human2-human1))

if ans == 1e10:
    print(-1)
else: print(ans)

