'''
2025.8.24
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

posi = list(map(int, input().split()))

#0~첫 가로등까지의 거리
#마지막 가로등 ~ 굴다리 끝까지의 거리 중 큰게 기준
h = max(posi[0], n-posi[-1])

while True:

    flag = True
    for i in range(m-1):
        if posi[i]+h < posi[i+1]-h: #다음 가로등에 닿지 x
            flag = False
            break

    if flag:
        #정답
        print(h)
        break
    else: #h + 1 갱신
        h += 1