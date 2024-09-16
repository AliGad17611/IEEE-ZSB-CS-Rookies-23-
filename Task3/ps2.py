n = int(input())
a = []
b = []
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
for c in range(num+1,len(b)):
    if m == b[c][1]:
        b.remove(b[c])
for i in range(0,len(b)):
    if s>b[i][1]:
        s =b[i][1]
        num = i
print(b[num][0])
for k in range(num+1,len(b)):
    if s == b[k][1]:
        print(b[k][0])
