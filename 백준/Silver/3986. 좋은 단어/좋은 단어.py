'''
2025.8.16
'''
import sys

input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    stack = []
    s = input().strip()
    for i in range(len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if len(stack) == 0:
        ans += 1
print(ans)
