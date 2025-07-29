import sys
from copy import deepcopy

def solve():
    # 입력 처리
    board = []
    for i in range(4):
        temp = list(map(int, input().split()))
        board_row = []
        for j in range(0, 8, 2):
            fish_num = temp[j]
            direction = temp[j+1] - 1  # 0-based indexing
            board_row.append((fish_num, direction))
        board.append(board_row)

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]  # 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
    dc = [0, -1, -1, -1, 0, 1, 1, 1]
    ans = 0

    def move_fish(board, shark_r, shark_c):
        # 물고기를 번호 순서대로 이동 (1~16)
        for target_fish in range(1, 17):
            # 현재 물고기 위치 찾기
            fish_r, fish_c = -1, -1
            for r in range(4):
                for c in range(4):
                    if board[r][c] and board[r][c][0] == target_fish:
                        fish_r, fish_c = r, c
                        break
                if fish_r != -1:
                    break
            
            # 물고기가 죽었으면 건너뛰기
            if fish_r == -1:
                continue
            
            fish_num, fish_dir = board[fish_r][fish_c]
            
            # 8방향 시도 (반시계방향으로 45도씩 회전)
            for _ in range(8):
                nr = fish_r + dr[fish_dir]
                nc = fish_c + dc[fish_dir]
                
                # 이동 가능한지 체크
                if (0 <= nr < 4 and 0 <= nc < 4 and 
                    not (nr == shark_r and nc == shark_c)):
                    
                    # 이동 실행
                    if board[nr][nc] is None:  # 빈 칸
                        board[nr][nc] = (fish_num, fish_dir)
                        board[fish_r][fish_c] = None
                    else:  # 다른 물고기와 위치 교환
                        board[fish_r][fish_c], board[nr][nc] = board[nr][nc], (fish_num, fish_dir)
                    break
                else:
                    # 방향 회전 (반시계방향)
                    fish_dir = (fish_dir + 1) % 8
                    board[fish_r][fish_c] = (fish_num, fish_dir)

    def dfs_move_shark(board, shark_r, shark_c, shark_d, eat_fish):
        nonlocal ans
        
        # 물고기 이동
        move_fish(board, shark_r, shark_c)
        
        # 상어 이동 시도
        moved = False
        step = 1
        
        while True:
            nr = shark_r + dr[shark_d] * step
            nc = shark_c + dc[shark_d] * step
            
            # 범위 체크
            if not (0 <= nr < 4 and 0 <= nc < 4):
                break
            
            # 물고기가 있는 칸만 이동 가능
            if board[nr][nc] is not None:
                moved = True
                
                # 현재 상태 백업
                board_backup = deepcopy(board)
                
                # 물고기 먹기
                fish_num, new_shark_dir = board[nr][nc]
                board[nr][nc] = None
                
                # 재귀 호출
                dfs_move_shark(board, nr, nc, new_shark_dir, eat_fish + fish_num)
                
                # 상태 복원
                board[:] = board_backup
            
            step += 1
        
        # 더 이상 이동할 수 없으면 답 갱신
        if not moved:
            ans = max(ans, eat_fish)

    # 게임 시작: (0,0) 물고기를 먹고 시작
    initial_fish_num, initial_shark_dir = board[0][0]
    board[0][0] = None
    
    # DFS 시작
    dfs_move_shark(board, 0, 0, initial_shark_dir, initial_fish_num)
    
    return ans

# 실행
if __name__ == "__main__":
    print(solve())