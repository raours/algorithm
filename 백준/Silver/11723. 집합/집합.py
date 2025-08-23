'''
2025.8.23
비트마스킹
'''
import sys
input = sys.stdin.readline

n = int(input())
bit = 0
for _ in range(n):
    senten = input().split()
    if len(senten) > 1:
        x,y = senten[0], int(senten[1])-1
        if x == 'add':
            bit = bit | (1<<y)
        elif x == 'remove':
            bit = bit & ~(1<<y)

        elif x == 'check':
            if bit & (1<<y) == 0:
                print(0)
            else:
                print(1)
        elif x == 'toggle':
            if bit & (1<<y) == 0:
                bit = bit | (1<<y)
            else:
                bit = bit & ~(1<<y)
    else:
        if senten[0] == 'all':
            bit = (1<<20) -1

        else:
            bit = 0
