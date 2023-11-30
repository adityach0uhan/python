De_=input("enter your marks in Digital electronics:")
pytho_n=input("enter your marks in python :")
os_=input("enter your marks in operating system :")
ds=input('enter your marks in data sructure :')
b=De_+pytho_n+os_+ds
a=b/4

if(a>100):
    print("please enter marks out of hundred in each subject")
elif(a>=80 ):
    print("you've got A grade ")
elif(a>=60):
    print("you've got grade B")
elif(a>=35):
    print("you've got  grade C")

else:
    print("you are failed")
     