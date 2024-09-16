import math
n = int(input())
for i in range(2,math.ceil(n**0.5)):
    while n%i==0:
        print(i,end=" ")
        n = n/i
