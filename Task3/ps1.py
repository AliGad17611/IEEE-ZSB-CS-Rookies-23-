n = int(input())
a = []
for i in range(0,n):
    row = list(input().split())
    a.append(row)
sumleft = sumright = 0
j = -1
for k in range(0,n):
    sumleft += int(a[k][k])
    sumright += int(a[j][k])
    j -= 1
result = sumleft - sumright
if result>=0:
    print(result)
else:
    print(result * -1)



