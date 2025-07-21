
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}

print("Enter your stock holdings.")
print("Type 'done' when finished.\n")

while True:
    stock_name = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock_name == 'DONE':
        break
    elif stock_name not in stock_prices:
        print("Stock not found in database. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_investment = 0
print("\n Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${price} = ${investment}")

print(f"\n Total Investment: ${total_investment}")

save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print(" Summary saved to 'portfolio_summary.txt'")
