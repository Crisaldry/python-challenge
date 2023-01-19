import os
import csv
import statistics

#importing csv file
#budget_data = os.path.join("..","Resources","budget_data.csv")
budgetdata = os.path.join("/Users/Crisaldry/Documents/GitHub/python-challenge/Instructions 8/PyBank/Resources/budget_data.csv")


# Variables
date = []
profit_losses = []
total_months = []
net_total = []
changes_profit_loss = []
greatest_increase = []
greatest_decrease = []
revenue_change = []
current_amount_PL = 0
previous_amount_PL = 0
average_change = []
greatest_increase_month = ""
greatest_decrease_month = ""
date_changes=[]



#opening csv file

with open(budgetdata, encoding="UTF") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #skip the headers
    
    for row in csvreader:
        date.append(row[0])
        current_amount_PL = int(row[1])
        profit_losses.append(current_amount_PL)
        
        #count number of months
        total_months = len(date)

        #count total revenue for the entire period
        net_total = sum(profit_losses)

        #changes in "profit/losses" over the enrite period + averages of those changes
        
        if len(profit_losses)> 1:
            previous_amount_PL = profit_losses[len(profit_losses)-2]
            changes_profit_loss.append(current_amount_PL - previous_amount_PL)
            average_change = round(float(statistics.mean((changes_profit_loss))),2)
            date_changes.append(row[0])

        #the greatest in profits (date and amount)

        greatest_increase = max(profit_losses)
        #greatest_increase_month = profit_losses.index(greatest_increase)- do not use
        idx_increase = profit_losses.index(greatest_increase)
        greatest_increase_month = date[idx_increase]

        #the greatest decrease in profits (date and amount)

        greatest_decrease = min(profit_losses)
        idx_decrease = profit_losses.index(greatest_decrease)
        greatest_decrease_month = date[idx_decrease]

#print the results
print("Financial Analysis"+"\n")
print("-----------------------------------"+"\n")
print("Total Months: "+str(total_months)+ "\n")
print("Total: $"+str(net_total)+"\n")
print("Average Change: $"+str(average_change)+"\n")
print("Greatest Increase in Profits: "+greatest_increase_month+" $"+str(greatest_increase)+"\n")
print("Greatest Decrease in Profits: "+greatest_decrease_month+" $"+str(+greatest_decrease)+"\n")

#write results in a text file 
with open("/Users/Crisaldry/Documents/GitHub/python-challenge/Instructions 8/PyBank/Resources/PyBank_Results.txt", mode="w") as resultfile:
    resultfile.write("Financial Analysis"+"\n")
    resultfile.write("-----------------------------------"+"\n")
    resultfile.write("Total Months: "+str(total_months)+ "\n")
    resultfile.write("Total: $"+str(net_total)+"\n")
    resultfile.write("Average Change: $"+str(average_change)+"\n")
    resultfile.write("Greatest Increase in Profits: "+greatest_increase_month+" $"+str(greatest_increase)+"\n")
    resultfile.write("Greatest Decrease in Profits: "+greatest_decrease_month+" $"+str(+greatest_decrease)+"\n")
