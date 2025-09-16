'''
2025.9.16
'''
import sys
input=sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

cnt = [0] * 10 #과일 종류 1~9!

ans = 0
start = 0
end = 0
cur = 0 #현재 과일 가짓 수
l = 0
while end<n:
    if cnt[lst[end]] == 0:  # 없던 종류가 추가되면,
        if cur < 2: #추가해도 되면,
            cur += 1
            cnt[lst[end]] += 1
            end += 1
            l += 1
        else: #추가 안되면,
            cnt[lst[start]] -= 1
            if cnt[lst[start]] == 0:
                cur -= 1
            start += 1
            l -= 1
    else: #있던 종류 추가면,
        cnt[lst[end]] += 1
        end += 1
        l += 1
    ans = max(ans, l)

    
print(ans)



