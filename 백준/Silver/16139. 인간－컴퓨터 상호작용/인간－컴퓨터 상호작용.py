'''
2025.9.6
'''
import sys

input=sys.stdin.readline

st = list(input().strip())
l = len(st)
n = int(input())

# 같은 문자열로 질문을 계속 한다함 = st를 기준으로 계속 구하면 됨!
# 누적합은 모든 알파벳 기준으로 2차원배열!
lst = [[0]*(l+1) for _ in range(26)]
for i in range(1, l+1):
    for j in range(26):
        if ord(st[i-1])-97 == j:
            lst[j][i] = lst[j][i-1]+1
        else:
            lst[j][i] = lst[j][i-1]

for _ in range(n):
    s, start, end = input().split()
    num = ord(s)-97 #아스키코드
    print(lst[num][int(end)+1]-lst[num][int(start)])
