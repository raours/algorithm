'''
2025.8.23
'''
import sys
input = sys.stdin.readline

n = int(input())

s = set()
for i in range(n):
    human, x = input().split()

    if x == 'enter': #출근
        s.add(human)
    else: #퇴근
        s.discard(human)
lst = sorted(s, reverse=True) #사전 순 역순
print(*lst, sep = '\n')