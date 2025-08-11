'''
2025.8.11
백준 : 단어  공부
'''
st = input().strip()
dic = {}
for s in st:
    if ord(s)>96: #소문자면
        s = chr(ord(s)-32) #대문자로 바꿔주고

    if s in dic: #나온 적 있는 문자면
        dic[s] += 1
    else:
        dic[s] = 1
new_s = sorted(dic.items(), key=lambda x: -x[1])

if len(new_s)>1 and new_s[0][1] == new_s[1][1]:
    print("?")
else:
    print(new_s[0][0])
