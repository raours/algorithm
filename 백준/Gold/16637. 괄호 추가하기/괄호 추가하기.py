'''
2025.7.31-8.2
백준 : 괄호 추가하기
'''
import sys

input = sys.stdin.readline

n = int(input())
s = list(map(str, input()))
for i in range(0,n,2): #숫자로 바꿔놓기
    s[i] = int(s[i])

def calculate(pre, mid, aft):
    if mid == '+':
        return pre+aft
    elif mid == '-':
        return pre-aft
    elif mid == '*':
        return pre*aft

ans = -1 * 2e32
def dfs(idx, value): #위치, 지금까지 계산한 값
    global ans
    #종료조건
    if idx == n-1:
        ans = max(ans, value)
        return
    #괄호 x: 순차적으로 계산, 그 다음부터 계산할 필요x
    if idx+2<n: #그 다음 연산자도 범위 안에 있으면,
        dfs(idx+2, calculate(value, s[idx+1], s[idx+2]))

    #괄호 o: 그 다음 연산자가 괄호로 묶여있어서, 뒤에부터 계산해야함
    if idx + 4 < n:
        dfs(idx+4, calculate(value, s[idx+1], calculate(s[idx+2],s[idx+3],s[idx+4])))

dfs(0, s[0])
print(ans)
