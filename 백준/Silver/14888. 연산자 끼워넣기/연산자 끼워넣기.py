
N = int(input())
A = list(map(int, input().split()))
cal = list(map(int, input().split()))
mx = -1e9
mn = 1e9


def dfs(n, temp):
    global mx, mn
    if n == N-1: #끝에 도달하면 return 해서 백트래킹
        mx = max(temp, mx) #왜 (mx, temp) 로 하면 틀릴까?
        mn = min(temp, mn)
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