n = int(input())
s = input().split()
st = ""
for i in range(0,len(s)):
    st = st + s[i]
num = int(st)
num += 1
st = str(num)
li = list(map(int,st))
for i in range(0,len(li)):
    print(li[i],end=" ")