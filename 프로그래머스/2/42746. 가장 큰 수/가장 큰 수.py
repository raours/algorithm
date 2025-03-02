
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)) #문자로 바꿔서 사전순으로 비교하기
    #문자를 3번 반복해서 길이 상관없이 비교할 수 있도록
    numbers.sort(key= lambda x : x*3, reverse =True) 
    
    for i in numbers:
        answer += i
    return str(int(answer))