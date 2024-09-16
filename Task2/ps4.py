s = input().split()
li = ""
for i in range(len(s)):
    li = li + s[i]
def clean_num(num):
    if len(num)==1 :
        return num
    if num[0]==num[1]:
        return clean_num(num[1:])
    return num[0] + " " + clean_num(num[1:])
# n = int(clean_num(li))
print(clean_num(li))