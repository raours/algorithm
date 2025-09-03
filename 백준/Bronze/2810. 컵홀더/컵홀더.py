'''
2025.9.3
'''
import sys

N = int(input())
seat = list(map(str, input().strip()))

cup = 1
second = 0
for i in range(N): # 좌석별!
    if seat[i] == 'S':
        cup += 1
    else:
        if second == 0: #첫 커플석이면,
            second = 1
        else:
            second = 0
            cup += 1
print(min(cup, N))
