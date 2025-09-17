'''
2025.9.18
'''
import sys
input=sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int, input().split()))


ans = 1e9
start = 0
end = 0
if lst[end] == 1:
    cur = 1 # 라이언 수 초기화
else:
    cur = 0
while end<n:
    if cur < k:  # 아직 두개 이하
        end += 1
        if end<n and lst[end] == 1:
            cur += 1

    else: #두개면
        ans = min(ans, end - start+1)
        if lst[start] == 1:
            cur -= 1
        start += 1

if ans == 1e9: print(-1)
else: print(ans)


