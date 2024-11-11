
lst = []
N = int(input())
a = list(input())

for _ in range(N):
    lst.append(int(input()))

stack = []

for i in a:
    if i.isalpha():
        stack.append(lst[ord(i)-65])
    else:
        sec = stack.pop()
        fir = stack.pop()
        if (i == '*'):
            stack.append(fir*sec)
        elif(i=='/'):
            stack.append(fir/sec)
        elif(i=='+'):
            stack.append(fir+sec)
        elif(i=='-'):
            stack.append(fir-sec)
        
print(format(stack[0],".2f"))

