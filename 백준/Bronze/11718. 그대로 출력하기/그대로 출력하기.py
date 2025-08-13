import sys

lines = sys.stdin.readlines() #파일의 끝 부분까지 한번에 가져옴
for line in lines:
    print(line.strip())