n = list(map(int,input().split()))
li = []
c = len(n)
for i in range(0,c):
    for j in range(i+1,c):
        if n[i]==n[j]:
            li.append(i)
            li.append(j)
for i in range(1,len(li),2):
    if c >= li[i]-li[i-1]:
        c = li[i]-li[i-1]
print(c)