'''
2025.7.13
백준 : 소수의 연속합
'''
import sys

input = sys.stdin.readline
n = int(input())

#에라토스테네스의 체
lst  = [i for i in range(n+1)] #n까지의 소수가 들어있는 곳!
end = int(n**(1/2)) #제곱근까지만!

for i in range(2,end+1): #2부터 제곱근까지 나눠지는 숫자는 out
    if lst[i] == 0: #이미 소수가 아니면, pass
        continue
    for j in range(i*i, n+1, i): #여기까지 왔으면, i는 소수임
        lst[j] = 0 #따라서 i의 배수들은 모조리 out

lst[1] = 0 #1은 소수가 아님!


#소수만 들어있는 list를 만들기
primary = []
for num in lst:
    if num != 0:
        primary.append(num)


ans = 0


for start in range(len(primary)): #시작점
    tmp,idx = 0, start
    de = []
    while True:
        if tmp == n: #성공! 경우의 수 +1
            ans += 1
            break
        elif tmp > n or idx>len(primary)-1: #실패
            break

        tmp += primary[idx]
        idx += 1

print(ans)