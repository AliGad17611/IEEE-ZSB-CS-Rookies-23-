x = input()
s = map(int,x)
n = list(s)
j=-1
c = 0
for i in range(0,len(n)):
    if n[i]!=n[j]:
        c +=1
    j -= 1
y=""
for i in range(-1,-len(n)-1,-1):
    y=y+x[i]
if c>0:
    print(int(y),"\nNO")
else:
    print(int(y),"\nYES")