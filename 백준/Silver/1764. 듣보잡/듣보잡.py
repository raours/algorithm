'''
2025.8.21
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
not_hear = set(input().strip() for _ in range(n))
not_look = set(input().strip() for _ in range(m))

not_hl = not_look & not_hear #교집합
# 사전순으로 정렬해야하기 때문에, sorted 함수를 이용하여 정렬된 리스트를 반환하자
# set은 순서가 없는 자료구조임!
ans = sorted(not_hl)
print(len(not_hl))
for i in ans:
    print(i)
