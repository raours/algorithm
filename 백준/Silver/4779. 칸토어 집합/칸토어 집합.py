'''
2025.9.7
'''
import sys

input=sys.stdin.readline
lines = sys.stdin.readlines() #전체 입력값 다 받아오기!

def cut(l):
    if l == 0: #길이 1이면(즉, 숫자 0입력이면), '-' 넘겨주기
        return '-'

    return cut(l-1)+' '* 3 ** (l-1)+cut(l-1) #이전 모양 + 빈칸 + 이전모양



for num in lines:
    print(cut(int(num)))