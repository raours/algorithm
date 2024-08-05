def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        
        a = s[0:step]
        cnt  =1
        len_sum = 0
        for i in range(step, len(s), step):
        
            if a == s[i:i+step]:
                cnt +=1
            else: 
                a = s[i:i+step]
                if cnt ==1:
                    len_sum += step
                    cnt =1
                else: 
                    len_sum += (step+len(str(cnt))) 
                    cnt=1
        if cnt ==1:
            len_sum += len(a)
        else: 
            len_sum += (len(a)+len(str(cnt))) 
        answer = min(answer, len_sum)
    return answer
                    
            