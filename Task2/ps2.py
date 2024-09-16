s = input()
c = 0
j = -1
n = (len(s)//2) + 1
for i in range(0,n):
    if s[i] != s[j]:
        c += 1
        break
    else:
        j -= 1
if c > 0 :
    print("no")
else:
    print("yes")