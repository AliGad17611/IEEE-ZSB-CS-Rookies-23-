n = int(input())
li = a =[]
for i in range(0,n):
    li1 = list(map(int,input().split()))
    li.append(li1)
for i in range(0,n):
    for j in range(n-1,-1,-1):
        print(li[j][i],end=" ")
    print("")