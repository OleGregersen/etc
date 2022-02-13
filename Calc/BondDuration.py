# Calculate bond duration

Yield = float(input("What is the yield of the bond? "))
Years = float(input("How many years to maturity? "))

MD = float(Years/(1 + Yield))
print("The modified duration of the bond is: ", round(MD, 2))
