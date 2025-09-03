import sys

x = int(input())

idx = 1
while True:
    if x - idx <= 0:      # idx가 n번째 줄, x가 n번째
        break
    else:
        x -= idx
        idx += 1

if idx % 2 == 0:          # 짝수 줄이면
    r = x
    c = idx - x + 1
else:                     # 홀수 줄
    r = idx - x + 1
    c = x

print(f"{r}/{c}")