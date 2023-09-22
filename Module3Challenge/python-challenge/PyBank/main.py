#import os to create file paths across operating systems and csv to read csv files
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#create lists to iterate through specific row
months = []
profit = []
monthly_profit_change = []


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
 #skip header  
    csv_header = next(csvreader)


#iterate through rows and append them to their corresponding lists
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
#iterate through rows to get monthly change and append monthly profit change
    for i in range(len(profit) -1):
        monthly_profit_change.append(profit[i+1]-profit[i])

#find the max/min of profit change and month and correlate to proper month in index
max_increase_profit = max(monthly_profit_change)
max_decrease_profit = min(monthly_profit_change)
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 



#print header for financial analysis
print("Financial Analysis")
print("---------------------------------")
#count the legnth of months
print(f"Total Months: {len(months)}")
#sum the profits
print(f"Total: ${sum(profit)}")
#find the average difference between each row of profit change
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
#find the greatest increase of profit and which month that was
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(max_increase_profit)})")
#find the greatest in proft and which month that was
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(max_decrease_profit)})")

