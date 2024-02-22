def calculate_amortization(principal, annual_interest_rate, years):
    # Convert annual interest rate to monthly and in decimal form
    monthly_interest_rate = annual_interest_rate / (12 * 100)

    # Convert years to months
    months = years * 12

    # Calculate amortization
    if monthly_interest_rate > 0:
        amortization = (principal * monthly_interest_rate * (1 + monthly_interest_rate)**months) / ((1 + monthly_interest_rate)**months - 1)
    else:
        amortization = principal / months

    return amortization