'''
2025.9.3
'''
import sys

input = sys.stdin.readline

n = int(input())

if 90<=n<=100:
    print('A')
elif 80<=n<90:
    print('B')
elif 70<=n<80:
    print('C')
elif 60<=n<70:
    print('D')
else:
    print('F')