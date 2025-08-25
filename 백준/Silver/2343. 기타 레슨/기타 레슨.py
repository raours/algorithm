'''
2025.8.25
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = max(lst) #무조건 맥스값보다는 크기가 크거나 같아야함
end = sum(lst)
ans = sum(lst)

while start <= end:
    mid = (start+end) // 2

    # mid를 블루레이 크기라고 했을 때, 계산
    cnt = 1
    minu = 0
    for i in range(n): #이렇게 계산하면 하나씩 더 포함하잖아.
        if minu+lst[i] <= mid: #아직 크기를 안넘는다면,
            minu += lst[i]
        else:
            cnt += 1
            minu = lst[i]

    if cnt <= m: #좀더 크기를 줄여도 됨
        ans = mid
        end = mid-1

    else:
        start = mid+1

print(ans)