n,k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-1, -1,-1):
    if k//lst[i]>0:
        ans += k//lst[i]
        k = k%lst[i]
        
    if k==0:
        break
print(ans)