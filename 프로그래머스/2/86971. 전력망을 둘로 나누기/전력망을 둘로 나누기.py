def dfs(a,chk,visit,lst):
    cnt = 1 #기준 노드
    visit[a] = True
    
    for i in lst[a]: #기준 노드와 연결된 모든 노드에 대해
        if not visit[i] and chk[a][i]: #연결된 간선이고 방문x인 노드라면
            cnt += dfs(i, chk, visit,lst) #그 노드를 다시 기준 노드로 설정해서 몇개 연결되어있는지 cnt에 저장
    return cnt #모든 조사 완료하면 cnt 반납 -> 자기 포함 몇개의 노드가 연결되어있는지

def solution(n, wires):
    answer = 1e9
    lst = [[] for _ in range(n+1)]
    for i in range(n-1):
        lst[wires[i][0]].append(wires[i][1])
        lst[wires[i][1]].append(wires[i][0])
    
    chk = [[True] *(n+1) for _ in range(n+1)] #노드 연결 되어 있는지
    
    #wires에서 하나씩 끊어본다
    for a,b in wires:
        visit = [False]*(n+1)
        chk[a][b] = False #연결 끊기
        chk[b][a] = False
        
        cnt_a = dfs(a,chk,visit,lst)
        cnt_b = n-cnt_a
        answer = min(answer, abs(cnt_a-cnt_b))
        
        chk[a][b] = True #다시 연결
        chk[b][a] = True
    
    
    return answer