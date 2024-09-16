n = int(input())
ranked = list(reversed(sorted(list(set(map(int,input().split()))))))
m = int(input())
plyer =list(map(int,input().split()))
for i in range(len(plyer)):
        if plyer[i] > ranked[0]:
            print(1)
        elif plyer[i]<ranked[-1]:
            print(len(ranked)+1)
        elif plyer[i] in ranked:
            print((ranked.index(plyer[i]))+1)
        else:
            for j in range(1,len(ranked)):
                if plyer[i]>ranked[j]:
                    print(j + 1)
                    break