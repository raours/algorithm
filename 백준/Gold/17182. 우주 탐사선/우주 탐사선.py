import sys

def recursive(start, cnt, cost):
    global result

    if cnt == n: #모든 행성을 방문했다면
        result = min(result, cost)
        return
    
    for next in range(n):
        if not visit[next]: #방문한 행성이 아니라면
            visit[next] = True
            recursive(next, cnt+1, cost+graph[start][next])
            visit[next] = False

n, k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

#플로이드 워셜 최단거리 구하기
for K in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][K]+graph[K][j])


# backtracking
visit =[False] * n
result = int(1e9)
visit[k] = True

recursive(k,1,0)
print(result)