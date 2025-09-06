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
lst = [[0]*26 for _ in range(2)] #첫번째 줄 모든 알파벳의 0번째 기준 !
lst[1][ord(st[0])-97] = 1 #첫번째 문자 체킹

for i in range(2, l+1): #i번째의 문자에 대한 누적합 만들어서 append
    lst.append(lst[i-1][:]) #복사해서 붙이기
    lst[i][ord(st[i-1])-97] += 1 #해당 문자에 대한 개수 카운팅만!

for _ in range(n):
    s, start, end = input().split()
    num = ord(s)-97 #아스키코드
    print(lst[int(end)+1][num]-lst[int(start)][num])
