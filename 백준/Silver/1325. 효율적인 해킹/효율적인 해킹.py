'''
2025.8.28
'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lst = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    lst[b].append(a)

def dfs(start):
    st = []
    st.append(start)
    visit[start] = 1 #방문 처리

    cnt = 0
    while st:
        cur = st.pop()

        for next in lst[cur]:
            if visit[next] == 0:
                st.append(next)
                visit[next] = 1
                cnt += 1

    return cnt


ans = [0]
for i in range(1, n+1):
    visit = [0] * (n + 1)
    ans.append(dfs(i))

mx = max(ans)

for i in range(1,n+1):
    if ans[i] == mx:
        print(i, end = ' ')

