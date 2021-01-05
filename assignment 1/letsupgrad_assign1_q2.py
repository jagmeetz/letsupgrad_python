z=0
x = input ("Enter username: ")
y = input ("Enter passowrd: ")
if x == "INDIA" and y== "IND":
    print("Login Successful")
elif x!= "INDIA":
    print(" Wrong Username")
elif y!= "IND":
    while z<4:
        print(" Wrong Password ")
        y = input ("Re-enter passowrd: ")
        z+=1
        if y == "IND":
            print("Login Successful")
            break 
    else:
        print("You have tried 5 times, cannot try for next 4 hours")
