def possible(answer):
    for x,y,a in answer:
        if a==0: #기둥이면
            if y ==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer:
                continue # 보가 있을 수도 있으니까 continue로 보일 때도 검사해야함 & 모든 좌표에 대해 검사해야함
            return False # 기둥인데 위에 조건에 안 맞으면 False
        else:
            if ([x-1,y,1] in answer and [x+1, y,1] in answer) or [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                continue
            else:
                return False
    return True # 모든 좌표에 검사가 끝났다면
                
        
        
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1: # 설치이면
            answer.append([x,y,a]) #일단 설치
            if not possible(answer): #가능한지 확인
               answer.remove([x,y,a]) #가능하지 않으면 삭제
        else: #삭제이면
            answer.remove([x,y,a]) #일단 삭제
            if not possible(answer): #가능한지 확인
               answer.append([x,y,a]) #가능하지 않으면 다시 설치
    return sorted(answer) 
            
        