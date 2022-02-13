# Calculate bond price

InterestRate = float(input("What is the spot interest rate? "))
Years = float(input("How many years to maturity? "))

BondPrice = float(1/(1 + InterestRate) ** Years)
print("The price of the discount bond is: ", round(BondPrice, 4))
