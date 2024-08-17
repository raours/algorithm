N = int(input())

A = list(map(int, input().split()))

cal = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(n, temp) :
    global mx, mn
    
    # 종료 조건
    if n == N-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return
     
    # 하부함수 호출
    if cal[0] != 0 : # 덧셈하는 경우
        cal[0] -= 1
        dfs(n+1, temp + A[n+1])
        cal[0] += 1 

    if cal[1] != 0 : # 뺄셈하는 경우
        cal[1]-= 1
        dfs(n+1, temp - A[n+1])
        cal[1] += 1
    
    if cal[2] != 0 : # 곱셈하는 경우
        cal[2] -= 1
        dfs(n+1, temp * A[n+1])
        cal[2] += 1
    
    if cal[3] != 0 : #나눗셈하는 경우
        cal[3] -= 1
        dfs(n+1, int(temp/A[n+1]))
        cal[3] += 1

dfs(0, A[0])
print(mx)
print(mn)