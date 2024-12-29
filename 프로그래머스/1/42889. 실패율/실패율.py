def solution(N, stages):
    total = len(stages)
    result = []
    
    for level in range(1,N+1):
        temp = stages.count(level)
        if total!=0: 
            r = temp/total
        else:
            r = 0
        total -= temp
    
        result.append((level,r))
    result.sort(key = lambda x: -x[1])   


    answer = []
    for arr in result:
        answer.append(arr[0])
    return answer