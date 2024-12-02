import sys
#소수 판별 때 숫자를 다 체크하면 시간 초과 됨
input = sys.stdin.readline
n=1000001
#1~10000까지의 수 중에서 에라토스테네스의 체를 이용해서 소수인지 판별해놓기 
arr = [True]*n
M =int(n**0.5)+1
for i in range(3, M,2):
    if arr[i]:
        for k in range(i*2, n, i):
            arr[k] = False


while(True):
    N = int(input())
    if N==0:
        break
    
    for a in range(3, int(N/2)+1,2):
        
        if arr[a] and arr[N-a]:
            print(f"{N} = {a} + {N-a}")
            break