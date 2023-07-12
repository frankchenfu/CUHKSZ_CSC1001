v=float(input("Enter the final account value:"))
r=float(input("Enter the annual interest rate:"))/100
t=float(input("Enter the number of years:"))
print("The initial value is:",v/(1+r)**t)