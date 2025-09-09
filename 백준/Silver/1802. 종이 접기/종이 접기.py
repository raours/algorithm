'''
2025.9.9
'''
import sys
input=sys.stdin.readline

def solve(lst):
    while len(lst)>=3:
        #접힌 후, 생성된 양 옆이 in, out이 서로 달라야 가능!
        for i in range(2, len(lst), 2):
            if lst[i-2] == lst[i]:
                return False

        next = []
        for i in range(1, len(lst),2):
            #이전 단계에 접힌 부분들 모으기
            next.append(lst[i])
        lst = next[:]

    return True




t = int(input())
for _ in range(t):
    lst = list(map(int,input().strip()))
    if solve(lst):
        print('YES')
    else:
        print('NO')

