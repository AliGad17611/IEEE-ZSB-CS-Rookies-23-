import random
z=random.randint(0,999)
s = list(map(int , str(z)))
while len(s)<3:
    s.insert(0,0)
ok = check = j = c = no = n = 0
m =4
while check <3:
    num = list(map(int , input("please guess the number and the number may be (000)or(999)or betwen them : ")))
    if len(num) != 3:
        print("The number consists of 3 digits ")
    else:
        for i in range(0,3):
            if num[i]==s[j]:
                ok += 1
                m = i
            else:
                no += 1
                if no == 2:
                    for k in range(0,3):
                        if k == m:
                            continue
                        else:
                            for y in range(0,3):
                                if num[k] == s[y]:
                                    n += 1
            j +=1
        print(ok,"hit",n,"miss")
        check = ok
    c += 1
    j = no = n = ok = 0
print("The number of attempts is :",c)