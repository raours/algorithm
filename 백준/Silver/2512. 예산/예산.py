'''
2025.8.25
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
total = int(input()) #국가 예산

#상한선의 최대를 구하자
start = 0 #min(lst) 하면 안됨! 상한선보다 큰 값들로 이루어진 list들을 총예산 안에 들어가도록 만들어야하는 경우도 있음
end = max(lst)

ans = 0 #min(lst) 하면 안됨! 상한선보다 큰 값들로 이루어진 list들을 총예산 안에 들어가도록 만들어야하는 경우도 있음
while start <= end:
    mid = (start+end) // 2

    #mid를 상한선으로 했을 때, 국가예산의 총액을 안 넘는다면,
    temp = 0
    for i in range(n):
        if lst[i]>mid:
            temp += mid #상한선 적용
        else:
            temp += lst[i]

    if temp <= total:
        ans = mid
        start = mid + 1 #상한선 더 높여보기
    else:
        end = mid - 1

print(ans)