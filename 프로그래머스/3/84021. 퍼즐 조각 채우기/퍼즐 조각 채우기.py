from collections import deque

def solution(game_board, table):
    n = len(game_board)

    # BFS로 블록 또는 빈 공간 추출 (좌표 집합 반환)
    def extract(board, target):
        visited = [[False]*n for _ in range(n)]
        results = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:
                    queue = deque([(i, j)])
                    visited[i][j] = True
                    shape = []

                    while queue:
                        x, y = queue.popleft()
                        shape.append((x, y))
                        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                    # 좌표 정규화
                    min_x = min(x for x, y in shape)
                    min_y = min(y for x, y in shape)
                    normalized = set((x - min_x, y - min_y) for x, y in shape)
                    results.append(normalized)
        return results

    # 90도 회전
    def rotate(block):
        return set((y, -x) for x, y in block)

    # 퍼즐 조각
    blocks = extract(table, 1)

    # 빈 공간
    empty_spaces = extract(game_board, 0)

    used = [False] * len(blocks)
    answer = 0

    for space in empty_spaces:
        matched = False
        for i, block in enumerate(blocks):
            if used[i]:
                continue
            rotated = block
            for _ in range(4):
                rotated = rotate(rotated)
                # 정규화
                min_x = min(x for x, y in rotated)
                min_y = min(y for x, y in rotated)
                normalized = set((x - min_x, y - min_y) for x, y in rotated)

                if normalized == space:
                    used[i] = True
                    answer += len(space)
                    matched = True
                    break
            if matched:
                break

    return answer
