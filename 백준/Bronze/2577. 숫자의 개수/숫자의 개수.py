a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c) #read problem!!

for i in range(10):
    print(num.count(str(i)))