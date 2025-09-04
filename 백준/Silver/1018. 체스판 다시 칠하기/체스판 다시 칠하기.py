'''
2025.9.3
'''
import sys
from collections import deque

n, m = map(int, input().split())
lst = [list(map(str, input().strip())) for _ in range(n)]

ans = []
for i in range(n-7): #시작점 고르기
    for j in range(m-7):
        white = 0 #시작, W일때
        black = 0 #시작, B일때

        for r in range(i, i+8):
            for c in range(j, j+8):
                #좌표의 합이 홀,짝,홀,짝 이런 식으로 구성되어 있다!
                if (r+c)%2 == 0: # (0,0)기준 W, B
                    if lst[r][c] == 'B':
                        white += 1 #W여야 하는데, B니까 +1
                    else:
                        black += 1 #B여야 하는데, W니까
                else: # 좌표 합 홀수 인 곳~!
                    if lst[r][c] == 'W':
                        white += 1 #B여야 하는데, W니까 +1
                    else:
                        black += 1 #W여야 하는데, B니까

        ans.append(min(black, white))

print(min(ans))
