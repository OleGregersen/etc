# Calculate future value

PresentValue = float(input("What is the present value? "))
InterestRate = float(input("What is the annual interest rate? "))
Years = int(input("How many years to reach future value? "))

FutureValue = float(PresentValue * (1 + InterestRate) ** Years)
print("Future Value is: ", round(FutureValue, 4))
