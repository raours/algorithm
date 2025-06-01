import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
answer = 1e9
for flst in lst: #각 번호에 대한 친구리스트를 모두 돌며 (a)
    for j in flst: # 그 번호에 대한 친구리스트 안의 한명을 선택 (b)
        for k in lst[j]: # (c) b의 친구리스트에 있는 c를 한명 골라서,
            if k in flst: #c가 a의 친구리스트에도 있다면, 셋은 친구!
                answer = min(answer, len(flst)+len(lst[j])+len(lst[k])-6)

if answer == 1e9:
    print(-1)
else: print(answer)