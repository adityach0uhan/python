num1=int(input("Enter the First Number :"))
num2=int(input("Enter the Second Number :"))
num3=int(input("Enter the Third Number :"))

# For Finding Greatest 
if(num1>num2 and num1>num3):
    print("Num 1 :",num1," is the Greatest")
elif(num2>num1 and num2>num3):
    print("Num 2 :",num2," is the Greatest")
else:
    print("Num 3 :",num3," is Greatest")    

# For Finding Smallest 
if(num1<num2 and num1<num3):
    print("Num 1 :",num1," is the Smallest")
elif(num2<num1 and num2<num3):
    print("Num 2 :",num2," is the Smallest")
else:
    print("Num 3 :",num3," is Smallest")        