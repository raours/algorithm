def balance(s):
    check = 0
    for i in range(len(s)):
        if s[i] == '(':
            check+=1
        else:
            check-=1
    if check ==0:
        return True
    else:
        return False
    
def correct(s):
    check = []
    for i in range(len(s)):
        if s[i] == '(':
            check.append('(')
        else:
            if check:
                check.pop()
            else:
                return False
    if len(check)==0:
        return True
    else:
        return False
    

def solution(p):
    answer = ''
    u = ""
    v = ""
    
    if len(p) == 0 or correct(p):
        return p
    
    for i in range(2,len(p)+1,2):
        temp = p[0:i]
        if balance(temp):
            u = temp
            v = p[i:]
            break
    
    if correct(u):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for j in range(1,len(u)-1):
            if u[j] == '(':
                answer += ')'
            else:
                answer += '('
    
    return answer