n = int(input())
li = []
sum1 = sum2 = sum3 = k = 0
c = -1
for i in range(0,n):
    s = input().split()
    sum1 += int(s[0])
    li.append(int(s[1]))
while k<=1:
    for j in range(0,len(li)):
        if sum3<=li[j] and (j!=c) :
            sum3 = li[j]
            q = j
    sum2 += sum3
    sum3 = 0
    c = q
    k += 1
if sum2>=sum1:
    print("Yes")
else:
    print("No")