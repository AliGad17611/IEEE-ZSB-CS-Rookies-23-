old_list = [[1,1,1],[1,1,1],[1,1,1]]
def cheak(i,j,k):
    old_list[i][j] += k
    if (j + 1)<3:
        old_list[i][j+1] += k
    if (j - 1)>=0:
        old_list[i][j - 1] += k
    if (i + 1)<3:
        old_list[i+1][j] += k
    if (i - 1)>=0:
        old_list[i-1][j] += k
for i in range(3):
    s = input().split()
    for j in range(3):
        cheak(i,j,int(s[j]))
for i in range(3):
    for j in range(3):
        if old_list[i][j]%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print("")
