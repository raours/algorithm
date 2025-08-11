'''
2025.8.11
백준 : OX퀴즈
'''

t = int(input())
for _ in range(t):
    st = input()
    con = 0
    score = 0
    for s in st:
        if s == 'O':
            con += 1
            score += con
        else:
            con = 0
    print(score)