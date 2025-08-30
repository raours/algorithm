'''
2025.8.30
'''
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())

s = []
def dfs():

        if len(s) == m: #모든 숫자 뽑았으면, return
            print(' '.join(map(str,s)))
            return

        for i in range(1, n+1):
            s.append(i)
            dfs()
            s.pop() #back tracking

dfs()
