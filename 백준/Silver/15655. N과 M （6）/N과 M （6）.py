'''
2025.9.3
'''
import sys

input = sys.stdin.readline

def dfs(start):

    if len(ans) == m: #n개 뽑았으면,
        print(*ans)
        return

    for i in range(start, n):
        ans.append(lst[i])
        dfs(i+1) #i+1 인덱스부터 또 dfs
        ans.pop()


n, m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort() #오름차순 정렬
ans = []

dfs(0)




