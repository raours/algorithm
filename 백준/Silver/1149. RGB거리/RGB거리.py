N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,N): #그 지점에 도달할 수 있는 경우 중 가장 적은 값으로 dp테이블 갱신
    lst[i][0] += min(lst[i-1][1], lst[i-1][2])
    lst[i][1] += min(lst[i-1][0], lst[i-1][2])
    lst[i][2] += min(lst[i-1][0], lst[i-1][1])

print(min(lst[N-1]))
