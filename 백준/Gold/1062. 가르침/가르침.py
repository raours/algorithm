'''
2025.7.10 - 7.11
백준 : 가르침
'''
from itertools import combinations
import sys

input = sys.stdin.readline


def change(word): #단어를 bit 방식으로 바꿔준다
    bit = 0
    for c in word:
        bit = bit | (1<< ord(c)- ord('a'))
    return bit

n, k = map(int, input().split())
words = [input().strip() for _ in range(n)]

words_bit = list(map(change, words)) # 남극의 단어들을 모두 비트로 변환한 리스트
base_bit = change('antic') #아는 단어 중 5개는 고정임

if k<5: #이미 아는 단어가 5개보다 더 많아야하므로,
    print(0)
else:
    letter = [1 << i for i in range(26) if not (base_bit & 1<<i)]
    ans = 0 #가장 많이 읽을 수 있는 단어 수 
    for combi in combinations(letter, k-5): #고정된 5개 제외하고 아는 단어 고르자!
        know_bit = base_bit | sum(combi) #아는 단어를 만들기(고정된 5글자와 sum으로 합쳐진 combi)
        cnt = 0 #읽을 수 있는 단어 셀 변수
        for w in words_bit: #남극의 단어들을 읽을 수 있는지 하나씩 체크
            if w & know_bit == w:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)