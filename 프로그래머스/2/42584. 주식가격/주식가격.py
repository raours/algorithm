def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n-1):
        cnt = 1 
        for j in range(i+1,n):
            if prices[i] > prices[j]: #가격이 떨어진 경우
                answer.append(cnt)
                break
            else:
                
                if j == n-1: #마지막까지 가격 안 떨어졌다면
                    answer.append(cnt)
                cnt += 1

    answer.append(0)
                
    return answer