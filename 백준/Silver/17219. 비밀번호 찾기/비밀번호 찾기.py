'''
2025.8.24
'''
import sys
input = sys.stdin.readline


n,m = map(int, input().split())

dic ={}
for _ in range(n):
    x,y = input().split()
    dic[x] = y

for _ in range(m):
    address = input().strip()
    print(dic[address])