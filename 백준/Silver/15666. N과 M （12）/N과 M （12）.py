'''
2025.9.3
'''
import sys

input = sys.stdin.readline

def dfs(start):

    if len(ans) == m: #n개 뽑았으면,
        print(*ans)
        return
    prev = None #같은 depth에서 똑같은 숫자로 시작하는 건 pass
    for i in range(start, n):
        if lst[i] != prev:
            ans.append(lst[i])
            dfs(i) #같은 수 여러번 가능!
            ans.pop()
            prev = lst[i] #현재 depth에서 선택했던 수 저장


n, m = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort() #오름차순 정렬
ans = []

dfs(0)




