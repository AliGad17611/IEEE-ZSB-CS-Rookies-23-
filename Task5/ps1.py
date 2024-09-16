import math
li = list(map(int,input().split()))
def swap(li,a,b):
    li[a],li[b]=li[b],li[a]
    return li
def reheap():
    for i in range(len(li)-1,-1,-2):
        parent = (math.ceil(i/2))-1
        child1 = (2*parent)+1
        child2 = (2*parent)+2
        if parent>=0:
            mx = max(li[child1],li[child2])
            if mx == li[child1]:
                index = child1
            else:
                index = child2
            if li[parent]< mx:
               swap(li,parent,index)
    for i in range(0,len(li)):
        parent = i
        child1 = (2*i)+1
        child2 = (2*i)+2
        if child2<len(li):
            mx = max(li[child1],li[child2])
            if mx == li[child1]:
                index = child1
            else:
                index = child2
            if li[parent]< mx:
               swap(li,parent,index)
               reheap()
reheap()
for i in range(len(li)):
    print(li[i],end=" ")

