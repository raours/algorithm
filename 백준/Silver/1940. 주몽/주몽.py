'''
2025.9.10
투포인터
'''
import sys
input=sys.stdin.readline


n = int(input())
m = int(input())

lst = list(map(int,input().split()))
ans = 0
lst.sort()

start = 0
end = n-1

while start < end:
    
    if lst[start] +lst[end] == m:
        ans += 1
        start += 1
    elif lst[start] +lst[end] > m:
        end -= 1
    else:
        start += 1
print(ans)

