def solution(brown, yellow):
    answer = []
    #br+ye 합을 2개의 곱셈으로 나타내면 됨 & 가로가 무조건 길다
    s = brown+yellow
   
    
    #그 곱셈의 조합 중, (가로+세로)*2-4 = brown인걸 찾으면 됨
    for i in range(1, int(s**(1/2)) + 1):
        if (s % i == 0):
            j = s // i
    
            if (i+j)*2-4 == brown:
                answer = [j,i]
                break
        
        
    return answer