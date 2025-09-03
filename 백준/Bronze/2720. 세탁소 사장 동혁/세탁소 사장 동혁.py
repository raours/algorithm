'''
2025.9.3
'''
import sys


T = int(input())

for _ in range(T):
    C = int(input())
    cnt = [0]*4

    q = C//25
    if q >0: #쿼터
        cnt[0] = q
        C -= 25*q

    dime = C//10
    if dime>0:
        cnt[1] = dime
        C -= 10*dime

    nickel = C//5
    if nickel > 0:
        cnt[2] = nickel
        C -= 5*nickel

    cnt[3] = C

    print(*cnt)