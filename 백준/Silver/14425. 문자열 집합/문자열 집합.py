
N,M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input().strip())
result = 0
for _ in range(M):
    a = input().strip()
    if a in S:
        result +=1

print(result)


