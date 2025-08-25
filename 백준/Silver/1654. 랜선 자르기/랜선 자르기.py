'''
2025.8.25
'''
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
k_lst = [int(input()) for i in range(k)]

start = 1
end = max(k_lst)

ans = 0
while start<= end:
    mid = (start+end)//2

    #k개 랜선, mid로 잘라보기
    temp = 0
    for i in range(k):
        temp += k_lst[i]//mid

    if temp >= n: #n개 이상 잘렸다면 mid를 더 높게!
        ans = mid
        start = mid + 1
    else:
        end = mid-1
print(ans)