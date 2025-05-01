def solution(tickets):
    answer = []
    visit = [False] * len(tickets)
    #dfs 티켓을 다 써보는거죠
    def dfs(start, path):
        if len(path) == len(tickets)+1: #티켓을 다 썼으면
            answer.append(path) #여러 루트가 있을 수 있으므로, append
        
        for idx,ticket in enumerate(tickets):
            if visit[idx] == False and ticket[0] == start:
                visit[idx] = True # 그 티켓을 씀
                dfs(ticket[1], path+[ticket[1]]) #그럼 다시 출발지는 그 티켓의 도착지가 되고, 지나온 공항path에 도착지를 추가
                visit[idx] = False #다른 경우도 찾기 위해 방문 안한걸로 다시 처리
                
                
    dfs("ICN", ["ICN"])            
    answer.sort() #알파벳순 정렬
    return answer[0]