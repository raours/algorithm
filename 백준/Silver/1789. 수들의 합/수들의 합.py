'''
2025.9.4
'''
import sys

s = int(input())

idx = 1
ans = 0
while s>0:
    s -= idx #1부터 계속 빼기
    ans += 1 #count
    idx += 1

if s == 0: #만약 딱 맞다면, 그게 답!
    print(ans)
else: #s<0면, 마지막 idx가 못 들어가는거니까 -1
    print(ans-1)

