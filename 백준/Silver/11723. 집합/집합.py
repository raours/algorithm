'''
2025.8.23
'''
import sys
input = sys.stdin.readline

n = int(input())

s = set()
for _ in range(n):
    senten = input().split()
    if len(senten) > 1:
        x,y = senten[0], int(senten[1])
        if x == 'add':
            s.add(y)
        elif x == 'remove':
            if y in s:
                s.discard(y)
        elif x == 'check':
            if y in s:
                print(1)
            else:
                print(0)
        elif x == 'toggle':
            if y in s:
                s.discard(y)
            else:
                s.add(y)
    else:
        if senten[0] == 'all':
            s = set(num for num in range(1,21))

        else:
            s = set()
