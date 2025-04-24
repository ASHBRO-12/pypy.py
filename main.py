actual_cost = float(input("Please enter the Actual Cost price."))
sale_amount = float(input("Please enter the Sale Amount."))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!")