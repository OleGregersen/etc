# Calculate effective interest rate

InterestRate = float(input("What is the annual interest rate? "))
Compoundings = int(input("How many compoundings in a year? "))

EffectiveRate = float((1 + InterestRate / Compoundings) ** Compoundings)
EffectiveInterestRate = float((EffectiveRate - 1) * 100)
print("Effective interest rate is: ", round(EffectiveInterestRate, 4), " %")
