high = num = int(input())
p = int(input())
c = n = low = 0
if p != 1:
    if p%2==0:
        p += 2
    else:
        p += 1
    if num%2==0:
        num += 2
    else:
        num += 1
    while n != p :
        if p > n :
            n = (low+high)//2
            if p>n:
                low=n
            if p<n :
                high = n

        else:
            n = (low + high) // 2
            if p > n:
                low = n
            if p < n:
                high = n

        c +=1
    c-=1
print(c)