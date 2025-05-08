def solution(genres, plays):
    answer = []
    dic = {}
    for i in genres:
        if not i in dic:
            cnt = 0
            for j in range(len(plays)):
                if genres[j] == i: # 그 장르 라면
                    cnt += plays[j] # +재생된 횟수
            dic[i] = cnt
    print( dic)
    
    tmp = []
    for idx, num in enumerate(plays):
        tmp.append((idx,dic[genres[idx]],num))
    tmp.sort(key = lambda x: (-x[1],-x[2],x[0]))
    print(tmp)
    
    visit = []
    for i in range(len(tmp)):
        if visit.count(tmp[i][1]) >= 2:
            continue
        answer.append(tmp[i][0])
        visit.append(tmp[i][1])
    return answer