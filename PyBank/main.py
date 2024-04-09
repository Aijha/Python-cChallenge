#Main Script

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses"
# The average

# The greatest increase in profits
# The greatest decrease in profits 

# Import Dependencies
import os
import csv

#Specify files
budgetcsv_path = os.path.join("/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyBank/Resources/budget_data.csv")

#Import and read CSV with  variables

with open(budgetcsv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader, None)
    
    data = list(csvreader)

    #set variables

    All_months = 0
    Net = 0
    ProfitDif = 0
    LossesDif = 0
    Profit_month = 0
    Losses_month = 0
    Avg_change = 0

    Above_row = 0
    Dif = 0
    Cml_difference = 0

 #Loop through to find total months
    for row in csvreader:

     #Count the total of months
        All_months += 1

     #Calculate the total revenue over the entire period
        Net = sum(int(row[1]) for row in data)
