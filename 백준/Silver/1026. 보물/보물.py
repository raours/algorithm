#백준 1026 보물
import sys

input = sys.stdin.readline

T = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


A.sort()
result = 0
for i in range(T):
    result += A[i]*max(B)
    B.remove(max(B))

print(result)