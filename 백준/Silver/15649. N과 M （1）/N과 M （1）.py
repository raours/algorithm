from itertools import permutations
N, M = map(int, input().split())
lst = []
for num in range(1,N+1):
    lst.append(num)

for i in permutations(lst,M):
    print(*i)