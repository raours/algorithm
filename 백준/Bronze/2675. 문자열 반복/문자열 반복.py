'''
2025.8.11
백준 : 문자열 반복
'''

T = int(input())
for _ in range(T):
    R,S = map(str, input().split())
    R = int(R)

    ans = ""
    for s in S:
        ans += (s*R)
    print(ans)