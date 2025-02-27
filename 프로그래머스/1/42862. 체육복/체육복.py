def solution(n, lost, reserve):
        
    # 여분의 체육복 있는 학생이 체육복 도난 당한 경우
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for student in sorted(reserve_set): #가장 작은 번호부터 빌려줄 수 있는 애 찾기
        if student-1 in lost_set:
            lost_set.remove(student-1)
        elif student+1 in lost_set:
            lost_set.remove(student+1)
    answer = n - len(lost_set) 
    
            
    return answer