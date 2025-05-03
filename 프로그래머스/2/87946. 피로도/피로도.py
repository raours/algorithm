from itertools import permutations
def solution(k, dungeons):
    answer = -1
    #순열로 인덱스의 순서를 만들어놓고
    n = len(dungeons)
    lst = []
    for p in permutations(range(n), n):
        lst.append(p)
        
    #그 인덱스의 순서대로 던전을 모두 돌고
    for i in lst:
        dun = 0
        kk = k
        for idx in i:
            if dungeons[idx][0]<=kk:
                kk -= dungeons[idx][1]
                dun += 1
                if dun == n:
                    return dun
            else:
                answer = max(answer, dun)
                break
    #가장 많이 간 던전의 개수를 답으로!
    return answer