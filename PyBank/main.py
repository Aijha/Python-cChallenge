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
budgetcsv_path = os.path.join("../Resources/budget_data.csv")

#Define Variables

totalmonths = []
netPL = []
monthlyPL = []
