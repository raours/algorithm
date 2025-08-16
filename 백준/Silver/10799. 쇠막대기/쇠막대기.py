'''
2025.8.15
'''
import sys

input = sys.stdin.readline

lst = input().strip()
stack = []
ans = 0
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
    else: # ) 일 때는 두가지 경우!
        stack.pop()
        if lst[i-1] == '(': #레이저인 경우
            ans += len(stack) #현재 열려있는 쇠막대기가 이 레이저에 의해 절단되어 열려있는 쇠막대기 개수만큼 생성
        else: #쇠막대기 끝인 경우,
            #그 쇠막대기는 닫히고, 맨 끝 한 조각만 추가
            ans += 1
print(ans)