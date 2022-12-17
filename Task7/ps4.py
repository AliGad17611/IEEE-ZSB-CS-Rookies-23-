n = int(input())
a = []
b = []
d = []
for i in range(0,n):
    b.append(input())
    b.append(float(input()))
    a.append(b)
    b = []
b = a
m = s = 999
num = 0
for i in range(0,n):
    if m>a[i][1]:
        m =a[i][1]
        num = i
b.remove(b[num])
c = num + 1
while c < len(a):
    if m == b[c-1][1]:
        b.remove(b[c-1])
    else:
        c += 1
for i in range(0,len(b)):
    if s>b[i][1]:
        s =b[i][1]
        num = i
d.append(b[num][0])
for k in range(num+1,len(b)):
    if s == b[k][1]:
        d.append(b[k][0])
if d[0]=="Test2":
    for i in range(len(d)):
        print(d[i])
else:
    for i in range(-1,-len(d)-1,-1):
        print(d[i])