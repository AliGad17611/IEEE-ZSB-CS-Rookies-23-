li1 = list(map(int,input().split()))
li = list(map(int,input().split()))
for i in range(0,len(li1)):
    li.append(li1[i])
c1=c2=c3=c4=c5=c6=c7=c8=c9=0
for i in range(0,len(li)):
    if li[i]==1:
        c1 += 1
    elif li[i] == 2:
        c2 += 1
    elif li[i] == 3:
        c3 += 1
    elif li[i] == 4:
        c4 += 1
    elif li[i] == 5:
        c5 += 1
    elif li[i] == 6:
        c6 += 1
    elif li[i] == 7:
        c7 += 1
    elif li[i] == 8:
        c8 += 1
    elif li[i] == 9:
        c9 += 1
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c1:
    print(1,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c2:
    print(2,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c3:
    print(3,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c4:
    print(4,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c5:
    print(5,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c6:
    print(6,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c7:
    print(7,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c8:
    print(8,end=" ")
if max(c1,c2,c3,c4,c5,c6,c7,c8,c9) == c9:
    print(9,end=" ")
