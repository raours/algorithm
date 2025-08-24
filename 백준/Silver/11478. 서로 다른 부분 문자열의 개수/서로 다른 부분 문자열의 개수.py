'''
2025.8.24
'''
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

if n == 1:
    print(1)
    exit()

part = set(s)
part.add(s)

if n == 2:
    print(len(part))
    exit()

for num in range(2,n): #부분 문자열
    for i in range(n-num+1):
        part.add(s[i:i+num])

print(len(part))