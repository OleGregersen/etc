# Calculate inflation adjusted return

InterestRate = float(input("What is the annual interest rate? "))
InflationRate = float(input("What is the annual inflation rate? "))

InflationAdjustedReturn = float((1 + InterestRate) / (1 + InflationRate))
RealRateOfReturn = float((InflationAdjustedReturn - 1) * 100)
print("Inflation adjusted return is: ", round(RealRateOfReturn, 4), " %")
