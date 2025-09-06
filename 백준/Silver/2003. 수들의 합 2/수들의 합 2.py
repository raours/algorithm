'''
2025.9.5
'''
import sys

input=sys.stdin.readline

n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
for i in range(2, n+1): #구간 합
    lst[i] += lst[i-1]

#투포인터
right = 1
left = 0
ans = 0

while right<= n and left <= right:
    temp = lst[right] - lst[left]
    if temp <m:
        right += 1 #구간합 증가시키기
    elif temp > m:
        left += 1 #구간 합 감소시키기
    else: #차랑 같은 걸 찾았으면!
        ans += 1
        right += 1 #다른 경우 찾기 위해!
print(ans)