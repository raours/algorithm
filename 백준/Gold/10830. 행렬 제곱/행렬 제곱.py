import sys
input = sys.stdin.readline

N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def mul(u,v):
    n = len(u)
    z = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            e = 0
            for k in range(n):
                e += u[i][k] * v[k][j]
            z[i][j] = e % 1000

    return z

def square(A,B):
    if B == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    #분할정복!
    tmp = square(A, B//2)
    if B % 2 == 0:
        return mul(tmp,tmp)
    else:
        return mul(mul(tmp,tmp),A)

ans = square(A,B)
for t in ans:
    print(*t)