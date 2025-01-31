import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j == i:
            lst[i][j] += lst[i-1][j-1]
        else:
            lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])
    
print(max(lst[N-1]))