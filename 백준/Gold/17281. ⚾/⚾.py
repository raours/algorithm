from itertools import permutations
import sys

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for perm in permutations(range(1,9),8): #4만개
    num = 0
    score = 0
    for i in range(N): #N개의 이닝에 대해
       temp_perm = list(perm)
       temp_perm = temp_perm[:3]+[0]+temp_perm[3:]

       out = 0
       base1 =base2=base3 =0 #베이스가 세개니까 단순하게 변수로 선언해서 주자가 있는지 없는지 기록
       while out<3:
           get_score = lst[i][temp_perm[num]]
           if get_score == 0: #out이면,
               out += 1
           elif get_score == 1: #안타
             score += base3
             base3 = base2
             base2 = base1
             base1 = 1
           elif get_score == 2:  # 2루타
               score += (base3+base2)
               base3 = base1
               base2 = 1
               base1 = 0
           elif get_score == 3:  # 3루타
               score += (base3 + base2+base1)
               base3 = 1
               base2 = 0
               base1 = 0

           elif get_score == 4:  # 홈런
               score += (base3 + base2 + base1+1)
               base3 = 0
               base2 = 0
               base1 = 0

           num = (num+1)%9

    ans = max(ans, score)
print(ans)