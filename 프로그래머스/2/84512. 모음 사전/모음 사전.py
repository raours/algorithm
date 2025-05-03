from itertools import product

def solution(word):
    answer = 0
        
    arr1 = ["A","E","I","O","U"]
    arr2 = []
    #문자로 사전만드는건 -> 중복순열 product!
    for i in range(1,6): 
        arr2.extend([("".join(p)) for p in list(product(arr1,repeat = i))])
    
    #그리고 인덱스 반환
    arr2.sort()
    answer = arr2.index(word)
    
    
    return answer+1