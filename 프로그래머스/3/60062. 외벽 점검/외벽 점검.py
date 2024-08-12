# 8/12 풀이 보고 풀었음/ 꼭 다시 풀기
from itertools import permutations

def solution(n, weak, dist):
    len_weak, answer = len(weak), len(dist) +1
    weak = weak + [i + n for i in weak]
    
    for start in range(len_weak): #모든 취약 지점에서 각각 시작해봄
        for friends in list(permutations(dist, len(dist))):
            cnt =1
            arrival = weak[start] + friends[cnt-1]
            for point in range(start, start+len_weak): 
                #친구들을 넣으며 취약점 정복 가능한지 check
                if arrival<weak[point]:
                    cnt +=1
                    if cnt>len(dist):
                        break
                    #다음 취약점부터 새 친구가 시작
                    arrival = weak[point] + friends[cnt-1] 
            answer = min(answer, cnt)
    
    if answer>len(dist):
        return -1
    return answer