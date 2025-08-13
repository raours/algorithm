'''
2025.8.14
백준 : 수 정렬하기
'''

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
for i in num:
    print(i)