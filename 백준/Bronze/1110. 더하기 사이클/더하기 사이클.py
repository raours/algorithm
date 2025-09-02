'''
2025.9.3
'''
import sys

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(1)
    exit()
cur = n
cycle = 0

while next != n:
    if cur <10: #한자릿 수,
        next = cur*11
    else:
        next = (cur%10)* 10 +( cur//10+cur%10 ) %10
    cur = next
    cycle += 1

print(cycle)




