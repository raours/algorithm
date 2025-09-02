'''
2025.9.3
'''
import sys

input = sys.stdin.readline

def dfs(start):

    if len(ans) == m: #n개 뽑았으면,
        print(*ans)
        return
    for i in range(start, len(lst)): #바뀐 길이만큼!
        ans.append(lst[i])
        dfs(i) #같은 수 여러번 가능!
        ans.pop()


n, m = map(int, input().split())
lst = sorted(set(map(int, input().split()))) #set으로 중복 제거 후 오름차순 정렬!
#어차피, 숫자 중복 사용 가능하니까, 굳이 depth 맏 따질 필요x
ans = []

dfs(0)


