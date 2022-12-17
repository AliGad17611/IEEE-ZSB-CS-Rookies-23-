p = int(input())
q = int(input())
kapreker_num =[]
for i in range(p,q+1):
    squre_num = str(i**2)
    if len(squre_num)>1:
        left_num = int(squre_num[:(len(squre_num)//2)])
        right_num = int(squre_num[(len(squre_num)//2):])
        new_num = left_num + right_num
    else:new_num = int(squre_num)
    if i == new_num:
        kapreker_num.append(i)
if len(kapreker_num)>0:
    for i in range(len(kapreker_num)):
        print(kapreker_num[i],end=" ")
else:
    print("INVALID RANGE")
