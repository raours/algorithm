def solution(array, commands):
    answer = []
    
    for i,j,k in commands:
        ans = array[i-1:j]
        ans.sort()
        answer.append(ans[k-1])
    return answer