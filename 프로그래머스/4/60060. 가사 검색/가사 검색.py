from bisect import bisect_left, bisect_right

def solution(words, queries):
    result = []
    a = [[] for _ in range(100001)]
    b = [[] for _ in range(100001)]
     
    for word in words:
        a[len(word)].append(word)
        b[len(word)].append(word[::-1])
        
    for i in range(1,100001):
        a[i].sort()
        b[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = bisect_right(a[len(q)], q.replace('?', 'z'))-bisect_left(a[len(q)], q.replace('?', 'a'))
        else:
            q = q[::-1]
            res = bisect_right(b[len(q)], q.replace('?', 'z'))-bisect_left(b[len(q)], q.replace('?', 'a'))
        result.append(res)
    
    return result
            