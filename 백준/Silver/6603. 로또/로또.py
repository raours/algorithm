'''
2025.8.30
'''
import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    temp_lst = list(map(int,input().split()))

    if temp_lst[0] == 0:
        break #종료
    lst = temp_lst[1:]

    for combi in combinations(lst,6):
        print(*combi)
    print()




