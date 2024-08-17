N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))
mx = -1000000000000 
#-1e9은 실수라서 max값이 10억이면 실수형이 출력되어 틀리게 됨
mn = 1000000000000 
#1e9 얘도 마찬가지. 따라서 초기화를 정수로 하던가 1e10, 1e+1 이런식으로 범위 밖의 값으로 초기화하기

def dfs(n, temp):
    global mx, mn
    if n == N-1: #끝에 도달하면 return 해서 백트래킹
        mx = max(mx, temp) 
        mn = min(mn, temp)
        return
    
    if cal[0] !=0:
        cal[0] -=1
        dfs(n+1, temp + A[n+1])
        cal[0] +=1  #백트래킹

    if cal[1] !=0:
        cal[1] -=1
        dfs(n+1, temp - A[n+1])
        cal[1] +=1

    if cal[2] !=0:
        cal[2] -=1
        dfs(n+1, temp * A[n+1])
        cal[2] +=1

    if cal[3] !=0:
        cal[3] -=1
        dfs(n+1, int(temp/A[n+1]))
        cal[3] +=1

dfs(0,A[0])
print(mx)
print(mn)