

print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
operator=input("Select an Operation you want to perform :")
a=input("enter your first number :")
b=input("enter your second number :")

if operator==1:
    print('on adding 'a, 'and'b,' we will get',a,b,a+b)

elif operator==2:
    print('on subtracting',a,'and',b,'we will get',a-b)

elif operator==3:
    print('on multiplying',a,'and',b,'we will get',a*b)
    
elif operator==4:
    print('on dividing',a,'and',b,'we will get',a/b)

else:
    print("you've press wrong key, may be")