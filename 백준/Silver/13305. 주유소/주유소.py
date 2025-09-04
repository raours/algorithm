'''
2025.9.4
'''
import sys

n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

temp_cost = 1000000001
passed = 0
ans = 0
for i in range(n-1):
    if temp_cost>cost[i]:
        #지금까지 지나온 거리 * 이전 최소 금액(temp_cost)
        ans += temp_cost*passed
        temp_cost, passed = cost[i], road[i]
    else: #현재 cost가 더 적으면,
        passed += road[i] #기름 안 넣고 지나치기
ans += temp_cost*passed #도착했으니, 마지막 계산
print(ans)
