'''
2025.8.15
'''
import sys

input = sys.stdin.readline

n = int(input())

stack = []
idx = 0
ans = []

num = 1
flag = True
for _ in range(n):
    su = int(input())

    while num <= su: #현재 주어진 수열의 요소보다 작거나 같아질 때까지 append
        stack.append(num)
        num += 1
        ans.append('+')

    # num == su 일 때거나 num이 su보다 커서 원래 stack에 있던걸 바로 pop해야하는 상황
    if stack[-1] == su: #같으면 pop
        stack.pop()
        ans.append('-')

    else:
        flag = False # 불가한 상황
        break

if flag:
    print(*ans,sep = '\n')
else:
    print("NO")

