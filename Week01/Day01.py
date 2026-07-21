#Mon Jul 20, 2026
#This code takes in the user's name first. Then, it capitalizes and strips the spaces to the left and right. Finally, the code greets the user.

name = input("What is your name? ")
name = name.capitalize().strip()
print(f"Hello, " , name)
