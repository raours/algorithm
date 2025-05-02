import itertools
def solution(numbers):
    answer = 0
    #문자를 배열로
    arr =[]
    arr2 = []
    for i in numbers:
        arr.append(i)
        arr2.append(int(i))
        
    temp = set(arr2)
    
    # 가능한 숫자 조합 만들기
    for i in range(2,len(arr)+1):
        nPr = set(itertools.permutations(arr, i)) #순열!
        for j in nPr:
            num = list(j)
            str = ''.join(num) #리스트를 바로 문자열로!
            temp.add(int(str)) #set에 add!
            # print(temp)
            
    # 소수 갯수 구하기
    def is_prime(x):
        if x == 0 or x==1:
            return False
        for i in range(2, int(x**(1/2))+1): 
            #2부터 제곱근 사이의 수로 나눠지면 -> 소수 아님!
            if x%i == 0:
                return False
        return True
        
    #가능한 숫자 조합들 temp에 대해 모두 판별
    for t in temp:
        if is_prime(t):
            answer += 1
    
    return answer