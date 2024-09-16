n,str_len=map(int,input().split())
list1 = []
list2 = []
for i in range(n):
    list1.append(list(map(int,input())))
const_count = 0
var_count = 0
mx = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(str_len):
            if list1[i][k]==1 or list1[j][k]==1:
                var_count += 1
        if var_count > mx:
            mx = var_count
            const_count = 1
        elif var_count == mx:
            const_count += 1
        var_count = 0
print(mx)
print(const_count)