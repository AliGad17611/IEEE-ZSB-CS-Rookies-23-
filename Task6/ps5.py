def hackerrankInString(s):
    a = 0
    for i in s:
        if a<10 and i == "hackerrank"[a]:
            a+=1
    return "YES" if a==10 else "NO"

for _ in range(int(input())):
    print(hackerrankInString(input()))
