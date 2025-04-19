# from collections import deque

# #BFS 코드
# def solution(n, computers):
#     visited = [0] * n
#     answer = 0
#     for i in range(n):
#         if visited[i]:
#             continue
#         visited[i] = 1
        
#         q = deque()
#         q.append(i)
    
#         while q:
#             now = q.popleft()
#             for j in range(n):
#                 if visited[j] == 0 and computers[now][j] == 1:
#                     q.append(j)
#                     visited[j] = 1 #방문 처리

#         answer += 1
             
    
    
#     return answer

#DFS 코드
def dfs(start,n,computers,visited):
    for i in range(n):
        if visited[i] == 0 and computers[start][i] == 1:
            visited[i] = 1 #방문 처리
            dfs(i,n,computers,visited)

def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    for i in range(n): #모든 노드에 대해
        if visited[i] == 0:
            visited[i] = 1 #방문처리
            dfs(i,n,computers,visited)
            answer += 1 #무리들 수 
        
    
    return answer