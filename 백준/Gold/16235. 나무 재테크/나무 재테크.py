'''
2025.7.16-7/17
백준 : 나무 재테크
'''
import sys

n,m,k = map(int,input().split())
robot = [list(map(int,input().split())) for _ in range(n)]
lst = [[5]*n for _ in range(n)] #양분 저장
tree_map = [[[] for _ in range(n)] for _ in range(n)] #그 자리에 나무 갯수
for i in range(m):
    x,y,z = map(int,input().split())
    tree_map[x-1][y-1].append(z)
    
def spring_summer():
    die = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(tree_map[i][j]) == 0: #나무 없으면, pass
                continue
            tree_map[i][j].sort(reverse = True) #내림차순 정렬
            flag = True
            temp = []
            for _ in range(len(tree_map[i][j])):
                a = tree_map[i][j].pop() #나무 나이
                if flag == False or lst[i][j] == 0 or lst[i][j] < a: #남은 양분 없거나 자기나이보다 양분 적으면
                    die[i][j] += a//2 # 여름에 양분 될 죽은 나무
                    continue #양분 없으면 즉시 죽으니까, 다시 넣을 필요x

                else: #남은 양분 있음
                    lst[i][j] -= a
                    temp.append(a+1)
            
            tree_map[i][j] = temp #양분 먹고 난 결과값 갈아끼우기
    
    for i in range(n):
        for j in range(n):
            lst[i][j] += die[i][j]
            
    return
        

def autumn():
    for i in range(n):
        for j in range(n):
            if len(tree_map[i][j]) == 0: #나무 없으면, pass
                continue
            
            for num in range(len(tree_map[i][j])):
                a = tree_map[i][j][num] #나무 나이
                if a %5 == 0: #5의 배수이면 번식
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)): #8방향
                        if 0<= i+dr <n and 0<= j+dc <n:
                            tree_map[i+dr][j+dc].append(1) #나이 1인 나무 번식!
    return
            

def winter():
    for i in range(n):
        for j in range(n):
            lst[i][j] += robot[i][j]
    return



for idx in range(k):
    spring_summer()
    autumn()
    winter()


ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree_map[i][j])

print(ans)
    