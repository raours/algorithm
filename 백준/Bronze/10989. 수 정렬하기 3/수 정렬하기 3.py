'''
2025.8.15
'''
import sys

n = int(input())
cnt = [0]*10001

#Counting Sort 계수정렬
for _ in range(n):
    cnt[int(input())] += 1


for i in range(1, 10001):
    if cnt[i]>0:
        for j in range(cnt[i]):
            print(i)