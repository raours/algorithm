# def dfs(begin, target, visit,words, dep):
#     if begin == target:
#         return dep
#     for i in range(len(words)):
#         if not visit[i]:
#             cnt = 0
#             for j in range(len(words[i])):
#                 if words[i][j] != begin: 
#                     cnt += 1
#             if cnt == 1:
#                 visit[i] = True
#                 dfs(words[i],target,visit,words, dep+1)
#                 visit[i] = False
    


# from collections import deque
# def solution(begin, target, words):
#     #변환 불가능하면 0 return
#     if not target in words:
#         return 0
#     n = len(words)
#     visit = [False] * n
    
#     ans = dfs(begin, target, visit, words, 0)
#     print(ans)
    
    
def dfs(begin, target, visit, words, depth, min_depth):
    if begin == target:
        min_depth[0] = min(min_depth[0], depth)
        return

    for i in range(len(words)):
        if not visit[i]:
            diff = sum(1 for a, b in zip(begin, words[i]) if a != b)
            if diff == 1:
                visit[i] = True
                dfs(words[i], target, visit, words, depth + 1, min_depth)
                visit[i] = False


def solution(begin, target, words):
    if target not in words:
        return 0

    visit = [False] * len(words)
    min_depth = [float('inf')]  # 리스트로 감싸야 참조 가능 (mutable)
    dfs(begin, target, visit, words, 0, min_depth)

    return 0 if min_depth[0] == float('inf') else min_depth[0]
