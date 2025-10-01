a=int(input("Enter your age:"))

#If statment no:1
if(a%2==0):
    print("A is even")
#End of If statment no :1

#If statment no:2
if(a>=5):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invaild negative age")

else:
    print("You are below the age of consent")
#End of If statment no :2

print("End of program")