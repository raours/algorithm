N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 0

for i in range(N):
    target = lst[i]
    start, end = 0, N - 1

    while start < end:
        # 자기 자신을 포함하지 않도록 처리
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        total = lst[start] + lst[end]

        if total < target:
            start += 1
        elif total > target:
            end -= 1
        else:  # total == target
            answer += 1
            break

print(answer)
