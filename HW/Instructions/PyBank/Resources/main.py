
import csv

profit = []
monthlyChanges = []
date = []

# Initialize the variables
 
count = 0
totalProfit = 0
totalChangeProfits = 0
initialProfit = 0

# Open the CSV using the set path PyBankcsv

with open ("C:/Users/Gisela Gutierrez/nu-chi-data-pt-09-2020-u-c/03-Python/HW/Instructions/PyBank/Resources/budget_data.csv", "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")      
    csv_header = next(csvReader)

    # Conducting the ask & counter
    for row in csvReader:    
      count = count + 1 

      # For collecting the greatest increase and decrease in profits
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      totalProfit = totalProfit + int(row[1])

      #Calculate the average change in profits month to month. Then calulate average change in profits
      finalProfit = int(row[1])
      monthlyChangeProfits = finalProfit - initialProfit

      #Store monthly changes in a list
      monthlyChanges.append(monthlyChangeProfits)

      totalChangeProfits = totalChangeProfits + monthlyChangeProfits
      initialProfit = finalProfit

      #Calculate the average change in profits
      averageChangeProfits = (totalChangeProfits/count)
      
      #Find the max and min change in profits and the corresponding dates these changes
      greatest_increase_profits = max(monthlyChanges)
      greatest_decrease_profits = min(monthlyChanges)

      increase_date = date[monthlyChanges.index(greatest_increase_profits)]
      decrease_date = date[monthlyChanges.index(greatest_decrease_profits)]
      
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(totalProfit))
    print("Average Change: " + "$" + str(int(averageChangeProfits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(totalProfit) +"\n")
    text.write("    Average Change: " + '$' + str(int(averageChangeProfits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

   




   
