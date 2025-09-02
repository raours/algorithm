'''
2025.9.3
'''
chk = [False] * 10001

for i in range(1,10001):
    sum_num = i
    st = str(i)

    for j in range(len(st)): #길이만큼!
        sum_num += int(st[j])
    if sum_num < 10001:
        chk[sum_num] = True

for i in range(1,10001):
    if not chk[i]:
        print(i)
