N = input()
lst = []
for i in range(len(N)):
    lst.append(int(N[i]))
half = len(lst)//2
if (sum(lst[0:half])==sum(lst[half:len(lst)])):
    print("LUCKY")
else:
    print("READY")