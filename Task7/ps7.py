#  this is code work on hackerrank

def chocolateFeast(n, c, m):
    count = n//c
    x = count
    while x>=m:
        a,b = divmod(x,m)
        count+=a
        x = a+b
    return count

for _ in range(int(input())):
    n,c,m = map(int,input().split())
    print(chocolateFeast(n, c, m))

# -----------------------------------------------------------
# this is my code but there's some problem
#
# n = int(input())
# list1 = []
# leftover = 0
# for i in range(n):
#     spend,cost,wrappers = map(int,input().split())
#     result1 = (spend//cost)
#     if wrappers > result1 :
#         leftover += (wrappers%result1)
#     if i == (n-1):
#         result2 = ((result1+leftover)//wrappers)
#     else:
#         result2 = (result1//wrappers)
#     result = (result1 + result2)
#     list1.append(result)
# for i in range(len(list1)):
#     print(list1[i])