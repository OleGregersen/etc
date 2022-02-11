# Calculate present value

FutureValue = float(input("What is the future value? "))
InterestRate = float(input("What is the annual interest rate? "))
Years = int(input("How many years to reach future value? "))

PresentValue = float(FutureValue / (1 + InterestRate) ** Years)
print("Present Value is: ", round(PresentValue, 4))
