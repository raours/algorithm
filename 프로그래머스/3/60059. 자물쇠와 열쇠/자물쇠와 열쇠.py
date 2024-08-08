def rotate(a): #열쇠 90도 회전
    n = len(a)
    result = [[0]*n for _ in range(n)] #회전한 열쇠 저장할 배열
    
    for i in range(n): 
        for j in range(n):
            result[j][n-1-i] = a[i][j]
    
    return result
    
def check(board): # 자물쇠 부분이 다 채워졌는지 확인
    n = len(board)//3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if board[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)    
    
    #비교를 위해 자물쇠 원래 크기 3배만큼 키우기
    board = [[0]*(n*3) for _ in range(n*3)]
    
    #board 중앙에 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            board[i+n][j+n] = lock[i][j]
            
    for rotation in range(4): #열쇠를 4방향으로 각각 회전시킬 때
        key = rotate(key)
        
        for x in range(2*n): #열쇠를 한칸씩 이동시키며
            for y in range(2*n):
                
                for i in range(m): #열쇠와 자물쇠 합체
                    for j in range(m):
                        board[x+i][y+j] += key[i][j]
                        
                if check(board) == True: # 자물쇠의 모든 홈을 열쇠로 메웠다면
                    return True
                
                for i in range(m): #열쇠와 자물쇠 분리
                    for j in range(m):
                        board[x+i][y+j] -= key[i][j]
    return False

    