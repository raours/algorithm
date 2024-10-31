N = int(input())
M = int(input())
S = input()

cursor, cnt, result = 0,0,0
while cursor<M-1:
    if S[cursor:cursor+3] == 'IOI':
        cnt +=1
        cursor +=2
        if cnt == N:
            result +=1
            cnt -=1
    else:
        cnt =0
        cursor +=1

print(result)
        