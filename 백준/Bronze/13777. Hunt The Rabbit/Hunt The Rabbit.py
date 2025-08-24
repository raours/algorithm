'''
2025.8.24
'''
import sys
input = sys.stdin.readline

while True:
    target = int(input())
    if target == 0:
        break
    start = 1
    end = 50

    while start<=end:
        mid = (start+end)//2

        if mid == target:
            print(target)
            break
        elif mid < target:
            start = mid +1
        else:
            end = mid-1
        print(mid, end=' ')

