'''
2025.9.4
'''
import sys

lst = [int(input()) for _ in range(10)]

total = 0
for i in range(1, 10):
    lst[i] += lst[i-1]
    if lst[i] == 100:
        print(100)
        break
    elif lst[i]>100:
        if lst[i]-100 <= 100 - lst[i-1]:
            print(lst[i])
            break
        else:
            print(lst[i-1])
            break
else: #넘지 않고 끝나면,
    print(lst[-1])

