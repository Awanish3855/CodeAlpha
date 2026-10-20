stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(stock, "-", price)

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found. Please choose from the list above.")
        continue

    quantity = int(input("Enter quantity: "))

    cost = stock_prices[stock_name] * quantity
    total_investment += cost
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    print(stock_name, "added. Cost:", cost)

print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    print(stock, ":", qty, "shares")

print("Total Investment Value: $" + str(total_investment))

save = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            f.write(stock + " : " + str(qty) + " shares\n")
        f.write("Total Investment Value: $" + str(total_investment) + "\n")
    print("Saved to portfolio_summary.txt")