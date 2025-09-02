'''
9/2

'''

def dfs(start):
    if len(choice) == M:
        print(*choice) # 선택된 배열이 M개와 같아졌을 경우 출력 후 return
        return
    pre = 0 # 내가 어떤 원소 담아줬는지 체크할 변수
    for i in range(start, N):
        if pre != arr[i]: 
            choice.append(arr[i]) # 선택한 원소 담고
            pre = arr[i] # 최근에 담은 원소 pre에 담아주기
            dfs(i) #중복허용이니까 다시 i부터
            choice.pop() # 다른 원소 넣기 위해 pop

N,M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
choice = []

dfs(0)