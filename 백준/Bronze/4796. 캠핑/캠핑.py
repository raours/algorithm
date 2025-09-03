'''
2025.9.3
'''
i = 1
while True:
    L,P,V = map(int,input().split())
    if (L,P,V) == (0,0,0):
        break
    period = V//P
    ans =  period * L
    V -= P*period

    if V<L:
        ans += V
    else:
        ans += L
    print(f"Case {i}: {ans}")
    i += 1