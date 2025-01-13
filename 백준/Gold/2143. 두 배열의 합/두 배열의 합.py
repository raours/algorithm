from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
alst = list(map(int, input().split()))
m = int(input())
blst = list(map(int, input().split()))

asum=[]
bsum=[]

#1. alst, blst의 누적합 구하기
for i in range(n):
    asum.append(alst[i])
    s = alst[i]
    for j in range(i+1, n):
        s += alst[j]
        asum.append(s)

for i in range(m):
    bsum.append(blst[i])
    s = blst[i]
    for j in range(i+1, m):
        s += blst[j]
        bsum.append(s)

#bisect (이진탐색) 할때는 무조건 정렬된 배열에서만 가능!
asum.sort()
bsum.sort()

answer =0
for i in range(len(asum)):
    r = bisect_right(bsum, T-asum[i])
    l = bisect_left(bsum, T-asum[i])
    answer += r-l

print(answer)

    
        
        