import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        a = heapq.heappop(scoville)
        if a>= K:
            break #충족
        if len(scoville) == 0:
            return -1 #할 수 없는 경우
        # print(scoville)
        
        b = heapq.heappop(scoville)
        next = a +2*b
        heapq.heappush(scoville,next)
        answer +=1
    
    return answer