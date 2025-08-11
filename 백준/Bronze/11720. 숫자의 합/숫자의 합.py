'''
2025.8.11
백준 : 숫자의 합
'''

n = int(input())
s = str(input())
ans = 0
for i in range(n):
    ans += int(s[i])
print(ans)