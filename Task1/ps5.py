n=int(input())
result = i =0
while (i<=n):
    if i%3==0 or i%5==0 :
        result += i
    i += 1
print(result)