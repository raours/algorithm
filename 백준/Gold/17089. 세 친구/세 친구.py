import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [set() for _ in range(N+1)]  # 리스트 → set

for _ in range(M):
    x, y = map(int, input().split())
    lst[x].add(y)
    lst[y].add(x)

answer = 1e9
for a in range(1, N+1):
    for b in lst[a]:
        for c in lst[b]:
            if c in lst[a] and a < b < c:  # 중복 제거: a < b < c 조건 추가
                total = len(lst[a]) + len(lst[b]) + len(lst[c]) - 6
                answer = min(answer, total)

if answer == 1e9:
    print(-1)
else:
    print(answer)
