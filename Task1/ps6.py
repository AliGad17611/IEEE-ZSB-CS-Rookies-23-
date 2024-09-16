n1 = int(input())
n2 = int(input())
if  n1<=n2:
    for i in range(1,n1+1):
        if (n1 % i == 0) and  (n2 % i == 0):
            result = i
else:
    for i in range(1, n2 + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            result = i
print(result)