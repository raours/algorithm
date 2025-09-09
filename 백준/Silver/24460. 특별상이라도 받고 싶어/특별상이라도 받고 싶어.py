'''
2025.9.9
'''
import sys
input=sys.stdin.readline

def solve(r,c,k):

    if k == 2:
        temp = [lst[r][c],lst[r+1][c+1],lst[r+1][c],lst[r][c+1]]
        temp.sort()
        return temp[1]
    if k>2:
        temp = []

        temp.append(solve(r,c,k // 2))
        temp.append(solve(r+k // 2,c,k // 2))
        temp.append(solve(r,c+k // 2,k // 2))
        temp.append(solve(r+k // 2,c+k // 2,k // 2))
        temp.sort()
        return temp[1]



n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]

if n == 1:
    print(lst[0][0])
else:
    print(solve(0,0,n))

