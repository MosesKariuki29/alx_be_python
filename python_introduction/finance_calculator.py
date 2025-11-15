# Ask the user for their monthly income
monthly_income = int(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate the monthly savings by subtracting monthly expenses from monthly income
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the monthly savings
print("Your monthly savings are $", monthly_savings)

# Display the projected annual savings after including interest
print("Projected savings after one year, with interest, is: $", projected_savings)
