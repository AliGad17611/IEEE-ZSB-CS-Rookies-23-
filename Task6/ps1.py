n_test = int(input())
list1 = []
count = 0
for i in range(n_test):
    list1.append(input())
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if int(list1[i][j])!=0 and int(list1[i])%int(list1[i][j])==0:
            count += 1
    print(count)
    count=0