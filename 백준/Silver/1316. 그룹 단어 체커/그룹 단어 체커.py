'''
2025.8.11
백준 : 그룹 단어 체커
'''
n = int(input())
ans = 0
for _ in range(n):
    st = input()
    word_list = []
    pre = ''

    flag = True
    for s in st:
        if pre != s: #앞 단어랑 다르면,
            if s in word_list: #예전에 나온 적 있다면,
                flag = False
                break #pass
            else: #처음 나온 단어
                word_list.append(s)
                pre = s
    if flag: ans += 1
print(ans)

