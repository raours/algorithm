'''
2025.8.30
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

s = []
def dfs(start):

        if len(s) == m: #모든 숫자 뽑았으면, return
            print(' '.join(map(str,s))) #오름차순으로 탐색 중이라 바로 출력 가능
            return

        for i in range(start, n+1):
            if i not in s:
                s.append(i)
                dfs(i)
                s.pop() #back tracking

dfs(1)
