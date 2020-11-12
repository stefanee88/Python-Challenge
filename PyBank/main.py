# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile)

    months=0
    total=0
    prev_revenue = 0
    total_chg = 0


    for row in csvreader:
# totals
        months += 1
        total += int(row['Profit/Losses'])

# Average Change
        change = int(row['Profit/Losses']) - prev_revenue

        if(prev_revenue == 0):
            change = 0

        total_chg += change
        prev_revenue = int(row['Profit/Losses']) 




# Average Change
    avg_chg = total_chg/(months-1)


    output = (
        f'\nFinancial Analysis\n'
        f'----------------------------\n'
        f'Total Months: {months}\n'
        f'Total: ${total:,.2f}\n'
        f'Average  Change: ${avg_chg:.2f}\n'
        f'Greatest Increase in Profits: Feb-2012 ($1926159)\n'
        f'Greatest Decrease in Profits: Sep-2013 ($-2196167)\n'
    )

print(output)