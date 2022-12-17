s = input()
year = int(s)+1
list1 = list(set(list(map(int,str(year)))))
while year>=1000 and year<=9000 and len(list1)<4 :
    year += 1
    list1 = list(set(list(map(int, str(year)))))
print(year)