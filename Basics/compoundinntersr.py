# PROGRAM FOR COMPOUND INTERSET
principal=float(input("Enter the principal amount :"))
rate=float(input("Enter the Interest Rate :"))
time=float(input("Enter the Time in years :"))
ci=principal*(pow((1+rate/100),time))

print('COMPOUND INTEREST IS :',ci)








