d1, m1, y1 = map(int,input().split())
d2, m2, y2 = map(int,input().split())
fine = 0
if y1==y2 and m1==m2 and d1<=d2:
    fine = 0
if y1==y2 and m1==m2 and d1>d2:
    fine += (d1-d2)*15
if y1==y2 and m1>m2:
    fine += (m1-m2)*500
if y1>y2:
    fine += (y1-y2)*10000
print(fine)