'''
2025.9.3
'''
import sys


T = int(input())

for _ in range(T):
    money = int(input())

    for coin in [25,10,5,1]:
        print(money//coin, end = ' ')
        money = money%coin
        