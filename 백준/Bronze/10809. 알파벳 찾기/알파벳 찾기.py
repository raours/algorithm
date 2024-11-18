S = input()
result = []
for i in range(26):
    temp = S.find(chr(97+i))
    if temp == -1:
        result.append(temp)
    else:
        result.append(temp)

for s in result:
    print(s, end=" ")