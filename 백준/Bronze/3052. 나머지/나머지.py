'''
2025.8.21
'''
import sys
input = sys.stdin.readline

s = set()
for _ in range(10):
    x = int(input())
    x = x%42
    s.add(x)

print(len(s))