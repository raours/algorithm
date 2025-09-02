'''
2025.9.3
'''
import sys


lines = sys.stdin.readlines() #입력 다 받아버리기
for line in lines:
    a, b = map(int, line.split())
    print(a+b)


