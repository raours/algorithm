'''
2025.8.11
백준 : 문자열 반복
'''

T = int(input())
for _ in range(T):
    R,S = input().split()
    for s in S:
        print(s*int(R), end='')
    print()
