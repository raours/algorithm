from collections import deque
def solution(begin, target, words):
    #변환 불가능하면 0 return
    if not target in words:
        return 0
    
    words.sort()
    n = len(words)
    answer = 0
    q = deque()
    q.append(begin)
    visit = [False] * n
    
    while q:
        before = q.popleft()
        
        if before == target:
            return answer
        
        for i in range(n):
            if not visit[i]: 
                num = 0
                after = words[i]
                
                for j in range(len(after)):
                    if before[j] != after[j]:
                        num += 1
                if num == 1: # 문자 하나만 다르면, 변환 가능
                    # print(after)
                    q.append(after)
                    visit[i] = True
                    answer += 1
                    break
            
    return 0