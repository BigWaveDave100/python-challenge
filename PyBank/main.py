# Dependencies
import csv

# Set variables
months = 0
net_profit_loss = 0
former_profit_loss = None
changes = []
greatest_increase = {"Date": None ,"Amount": float('-inf')}
greatest_decrease = {"Date": None ,"Amount": float('inf')}
# Skip header row and loop through csv file
with open("PyBank/Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        months += 1
        net_profit_loss += profit_loss
        # determine change in Profit/Loss margin 
        if former_profit_loss is not None:
            change = profit_loss - former_profit_loss
            changes.append(change)
            # Determine greatest increase and the date associated
            if (change > greatest_increase["Amount"]):
                greatest_increase["Amount"] = change
                greatest_increase["Date"] = date
            # Determine greatest decrease and the date associated
            if (change < greatest_decrease["Amount"]):
                greatest_decrease["Amount"] = change
                greatest_decrease["Date"] = date
        
        former_profit_loss = profit_loss
# Determine and calculate average change in profit
if changes:
    average_change = sum(changes)/len(changes)
else:
    average_change = 0
#Display results
results = [
    f"Financial Analysis",
    f"-------------------",
    f'Total Months = {months}',
    f'Total Profit/Loss = ${net_profit_loss}',
    f'Average Change = ${average_change:.2f}',
    f'Greatest Profit Increase = {greatest_increase["Date"]} (${greatest_increase["Amount"]})',
    f'Greatest Profit Decrease = {greatest_decrease["Date"]} (${greatest_decrease["Amount"]})',
]
# terminal print
for result in results:
    print(result)

# text file
with open('financial_analysis.txt', 'w') as txtfile:
    for result in results:
        txtfile.write(result + '\n')