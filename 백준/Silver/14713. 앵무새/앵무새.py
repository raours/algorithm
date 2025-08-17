'''
2025.8.17
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sentence = [deque(input().split()) for _ in range(n)]
l = list(input().split())


for i in range(len(l)):
    x = l[i]
    flag = False
    for j in range(n):
        if sentence[j] and sentence[j][0] == x:
            sentence[j].popleft()
            flag = True
            break
    if not flag:
        print("Impossible")
        exit()

for i in range(n):#앵무새가 말한 단어는 모두 포함되어야함
    if len(sentence[i]) != 0:
        print("Impossible")
        exit()
print("Possible")
