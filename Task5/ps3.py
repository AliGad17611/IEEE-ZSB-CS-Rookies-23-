attractors = [2,4,16,37,58,89,145,42,20]
sum=int(input())
li = list(map(int,str(sum)))
if sum in attractors:
    print("false")
else:
    if sum == 1:
        print("true")
    while sum != 1:
        sum = 0
        for i in range(len(li)):
            sum += (li[i]**2)
        li = list(map(int,str(sum)))
        if sum in attractors:
            print("false")
            break
        else:
            if sum == 1:
                print("true")


