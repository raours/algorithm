'''
2025.7.13
백준 : 소수의 연속합
'''
import sys

input = sys.stdin.readline
n = int(input())

if n == 1:
    print(0)
    exit(0)

#에라토스테네스의 체
lst  = [True] * (n+1) #n까지의 소수가 들어있는 곳! boolean으로 체크하면 효율적
end = int(n**(1/2)) #제곱근까지만!
lst[0] = False
lst[1] = False #0,1은 소수가 아님

for i in range(2,end+1): #2부터 제곱근까지 나눠지는 숫자는 out
    if not lst[i]: #이미 소수가 아니면, pass
        continue
    for j in range(i*i, n+1, i): #여기까지 왔으면, i는 소수임
        lst[j] = False #따라서 i의 배수들은 모조리 out

#소수만 들어있는 list를 만들기
primary = []
for i in range(2,n+1):
    if lst[i]:
        primary.append(i)


ans = 0
total = primary[0]
start,end = 0, 0

while True:
    if total>=n: #합보다 크면 start값 +1, 맨 왼쪽 소수 빼기
        if total == n: #같으면, 성공! ans + 1
            ans += 1
        total -= primary[start]
        start += 1 
    elif end == len(primary)-1: #end값이 끝까지 도달했으면 break
        break
    else: #합보다 작으면 end값 +1, 새로운 오른쪽 소수 더하기
        end += 1 
        total += primary[end]
        

print(ans)