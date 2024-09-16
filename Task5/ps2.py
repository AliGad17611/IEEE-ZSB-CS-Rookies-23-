user_input = input()
count = 0
if len(user_input)<=1:
    count += 1
else:
    for i in range(1,len(user_input),2):
        if (user_input[i-1]=="(") and (user_input[i]!=")"):
            count += 1
            break
        if (user_input[i-1]=="{") and (user_input[i]!="}"):
            count += 1
            break
        if (user_input[i-1]=="[") and (user_input[i]!="]"):
            count += 1
            break
if count == 0:
    print("true")
else:
    print("false")



