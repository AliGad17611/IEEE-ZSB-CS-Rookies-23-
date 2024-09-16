user_input = input()
i = 0
while i < len(user_input):
    if user_input[i] == ".":
        print(0, end="")
        i += 1
    elif user_input[i]=="-" and user_input[i+1]==".":
        print(1, end="")
        i += 2
    elif user_input[i]=="-" and user_input[i+1]=="-":
        print(2, end="")
        i += 2
