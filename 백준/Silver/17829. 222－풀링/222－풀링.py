'''
2025.9.8
'''
import sys

input=sys.stdin.readline

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

def solve(lst,n):
    if n == 1:
        return lst[0][0] #결과 값

    #2x2로 나눠서 2번째로 큰 수 추출하는 과정 반복
    temp = [[0]*(n//2) for _ in range(n//2)] #압축될 애들 저장할 배열
    for i in range(n//2):
        for j in range(n//2):
            #2번째 최대값 구하기 위한 배열: 2x2 내의 원소들 모두 append
            l = sorted(lst[i*2][j*2:j*2+2]+lst[i*2+1][j*2:j*2+2]) #아랫줄, 윗줄
            temp[i][j] = l[-2]

    return solve(temp, n//2) #압축된 애들에 대해 또, 압축 (재귀)


print(solve(lst,n))