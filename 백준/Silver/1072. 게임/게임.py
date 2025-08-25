'''
2025.8.25
'''
import sys
input = sys.stdin.readline

x, y = map(int, input().split())

target =(y* 100)//x
if target>98: #승률 99,100이면 더이상 높아질 수 x
    print(-1)
    exit()

start = 1
end = x
ans = 0

while start<=end:
    mid = (start+end)//2
    if int((y+mid) * 100)//(x+mid) > target: #승률 높으면, 그리고 정수연산으로 하기!(부동소수점)
        ans = mid
        end = mid-1
    else:
        start = mid +1

print(ans)