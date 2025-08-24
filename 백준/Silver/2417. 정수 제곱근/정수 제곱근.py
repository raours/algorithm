'''
2025.8.24
'''
import sys
import decimal
input = sys.stdin.readline

n = int(input())

r = decimal.Decimal(str(n)).sqrt() #부동소수점 문제 해결
r = int(r)
print(r if r*r==n else r+1)