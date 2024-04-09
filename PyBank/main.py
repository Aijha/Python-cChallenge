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

    All_months = len(data)
    Net = 0
    ProfitDif = 0
    LossesDif = 0
    max_increase = 0
    max_decrease = 0
    Avg_change = 0


 #Loop through to find total months
    for row in csvreader:
        All_months = len(data)

     #Calculate the total revenue over the entire period
    Net = sum(int(row[1]) for row in data)

# 3. Changes in "Profit/Losses" over the entire period, and then the average of those changes
ProfitDif = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, len(data))]
Avg_change = sum(ProfitDif) / len(ProfitDif)

# 4. Greatest increase in profits (date and amount) over the entire period
max_increase = max(ProfitDif)
max_increase_index = ProfitDif.index(max_increase) + 1  # Adding 1 because of skipped header row
max_increase_date = data[max_increase_index][0]

# 5. Greatest decrease in profits (date and amount) over the entire period
max_decrease = min(ProfitDif)
max_decrease_index = ProfitDif.index(max_decrease) + 1  # Adding 1 because of skipped header row
max_decrease_date = data[max_decrease_index][0]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {All_months}")
print(f"Total Profit/Loss: ${Net}")
print(f"Average Change: ${Avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

#Write changes to csv

output_path = os.path.join("/Users/aijhasymone/Desktop/ClassFolder/Python-cChallenge/PyBank/output.csv")


with open(output_path, 'w', newline = '') as file:
    csvwriter = csv.writer(file, delimiter=':')
    
    # header row
    csvwriter.writerow(["Metric", "Value"])
    
    csvwriter.writerow(["Total Months", All_months])
    csvwriter.writerow(["Total", Net])
    csvwriter.writerow(["Average Change", Avg_change])
    csvwriter.writerow(["Greatest Increase in Profits", f"{max_increase_date}:{max_increase}"])
    csvwriter.writerow(["Greatest Decrease in Profits", f"{max_decrease_date}:{max_decrease}"])

print(f"Results have been written to {output_path}")
