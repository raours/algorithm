'''
2025.8.30
'''
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

s = []
def dfs():

        if len(s) == m: #모든 숫자 뽑았으면, return
            print(' '.join(map(str,s)))
            return

        for i in range(n):
            if lst[i] not in s:
                s.append(lst[i])
                dfs()
                s.pop() #back tracking

dfs()
