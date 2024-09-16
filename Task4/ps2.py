li1 = input()
li = input()
li2 = ""
for i in range(len(li1)-1,-1,-1):
    li2 = li2 +li1[i]
if li2 in li:
    print("True")
else:
    print("False")