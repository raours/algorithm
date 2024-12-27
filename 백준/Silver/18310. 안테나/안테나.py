import sys

input = sys.stdin.readline
N = int(input())
house = list(map(int, input().split()))

house.sort()
answer = 0
if N%2 == 0 :
    answer = house[N//2-1]
else :
    answer = house[N//2]

print(answer)