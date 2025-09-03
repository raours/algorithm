'''
2025.9.3
'''
import sys

money = 1000-int(input())

ans = 0
for coin in [500,100,50,10,5,1]:
    ans += money//coin
    money = money%coin
print(ans)