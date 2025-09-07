'''
2025.9.7
'''
import sys

input=sys.stdin.readline
lines = sys.stdin.readlines() #전체 입력값 다 받아오기!

def cut(s,n):
    if n == 1:
        return
    for i in range(s + n//3, s +(n//3)*2):
        result[i] = ' '
    cut(s, n//3)
    cut(s + n//3 * 2, n//3)


for num in lines:
    num = 3**int(num)

    result = ['-'] * num  # 최초 리스트 집합
    cut(0, num)  # 자르기
    print(''.join(result))
