from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    visit = [0] * n
    q = deque()
    q.append((0, numbers[0]))
    q.append((0, -numbers[0]))
    visit[0] = 1
    # print(q)
    
    while q:
        index, total = q.popleft()
        index += 1
        
        if index < n:
            q.append((index, total+numbers[index]))
            q.append((index, total-numbers[index]))
       
        elif total == target:
                answer += 1
                

    
    return answer