s = input().strip()
temp = ''
flag = False
lst = []

for i in range(len(s)):
    if s[i].isdigit():
        temp += s[i]
    else:
        lst.append(int(temp))
        temp = ''
        lst.append(s[i])

lst.append(int(temp))

ans = 0
for j in range(len(lst)):
    if j % 2 == 0:  # 숫자
        if flag:
            ans -= lst[j]
        else:
            ans += lst[j]
    else:
        if lst[j] == '-':
            flag = True
            
print(ans)