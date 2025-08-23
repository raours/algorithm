'''
2025.8.23
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

ab1 = a|b #합집합
ab2 = a&b #교집합

print(len(ab1)-len(ab2))