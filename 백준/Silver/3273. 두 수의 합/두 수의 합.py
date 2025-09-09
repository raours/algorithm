'''
2025.9.10
'''
import sys
input=sys.stdin.readline



n = int(input())
lst = list(map(int,input().split()))
x = int(input())
lst.sort() #정렬부터!

start = 0
end = n-1
ans = 0
while start<end:

    num = lst[start]+lst[end]
    if num == x:
        ans += 1
        start += 1
    elif num>x:
        end -= 1
    else:
        start += 1

print(ans)