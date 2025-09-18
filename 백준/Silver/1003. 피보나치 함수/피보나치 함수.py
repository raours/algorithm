'''
2025.9.18
'''
import sys
input=sys.stdin.readline

t = int(input())
fibo_1 = [0]*41
fibo_0 = [0]*41
fibo_0[0] = 1
fibo_1[1] = 1
for _ in range(t):
    n = int(input())

    for i in range(2,n+1):
        fibo_0[i] = fibo_0[i-1]+fibo_0[i-2]
        fibo_1[i] = fibo_1[i-1]+fibo_1[i-2]

    print(fibo_0[n],fibo_1[n])


