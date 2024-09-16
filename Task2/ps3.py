s = input()
k = 0
def cleanword(word,m):
    if len(word)==1 :
        return word
    if word[0]==word[1] and m < 2:
        m += 1
        return cleanword(word[1:],m)
    m = 0
    return word[0] + cleanword(word[1:],m)
print(cleanword(s,k))
st = cleanword(s,k)
if "hello" in st:
    print("YES")
else:
    print("NO")
