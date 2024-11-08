N = int(input())
result = []

for _ in range(N):
    lst = input()
    if lst[:2] == 'pu':
        result.append(int(lst[5:]))
    elif lst[:2] == 'po':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
            result.pop()
    elif lst[:2] == 'si':
        print(len(result))
    elif lst[:2] == 'em':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif lst[:2] == 'to':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])

