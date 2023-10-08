# Given values
RSS = 44  # Residual Sum of Squares
TSS = 80  # Total Sum of Squares
# Calculate R-squared
R_squared = 1 - (RSS / TSS)
# Round R-squared to two decimal places
R_squared = round(R_squared, 2)
# Print the result
print("The coefficient of determination (R-squared) is:", R_squared)
