'''
2025.8.20
'''
import sys
import heapq
input = sys.stdin.readline

hq = []
n, h, t = map(int, input().split())
for _ in range(n): # 거인들의 키, 최대 힙에 넣기
    heapq.heappush(hq, -int(input()))
flag = True
yes_ans = 0
while True:
    x = -heapq.heappop(hq)
    if x >= h and t>0 and x>1: #뿅망치 hit
        heapq.heappush(hq, - (x//2)) #연산자 우선순위로 -x//2이렇게 하면 (-x)//2 이렇게 계산돼서
        # 계속 의도보다 1씩 작은 수가 저장됨
        t -= 1
        yes_ans += 1
    elif x >= h:
        if t<= 0 or x <= 1: #실패
            flag = False
            no_ans = x
            break
    elif x<h:
        #성공
        break

if flag:
    print("YES")
    print(yes_ans)
else:
    print("NO")
    print(no_ans)