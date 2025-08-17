'''
2025.8.17
'''
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split())) #스택 or 큐인지
b = list(map(int, input().split()))

m = int(input())
m_lst = list(map(int, input().split()))
q = deque()
for i in range(n):
    if a[i] == 0: # 큐만 리턴 값에 영향을 줌!
        # 큐들을 이어 하나의 큰 큐로 생성하기!
        # 리턴값만 알면 되므로 어떤 큐에 있던 값인지 알 필요x
        q.append(b[i])

ans = []
for x in m_lst:
    q.appendleft(x)
    ans.append(q.pop())
print(*ans)