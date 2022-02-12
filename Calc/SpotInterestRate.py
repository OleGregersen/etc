# Calculate spot interest rate

BondPrice = float(input("What is the price of the discount bond? "))
Years = float(input("How many years to maturity? "))

SpotPrice = float(1/(BondPrice ** (1/Years) - 1))
print("The spot interest rate is: ", round(SpotPrice, 4))
