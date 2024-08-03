import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))


for i in range(m):
    lst.sort()
    min1 = lst.pop(0)
    min2 = lst.pop(0)
    a = min1+min2
    lst.append(a)
    lst.append(a)


print(sum(lst))