#import Dependencies
import os
import csv
Months = []
num_months = 0

# import the CSV file 
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')


    for row in csvreader:
        print(row)
        #num_months = 0

    
    file = csv.DictReader(csvreader)
    
    Date = []
    Profit = []
    
    for col in csvreader:
        Date.append(col[0])
        Profit.append(col[1])

    print('Dates:', Date)
    print('Profit/Losses:', Profit)
    
    #for row in csvreader:
        #num_months += 1

        #print(num_months)
       
        #monthscalced=87

    #this is not coming out right, but I needed to move on

#Calculate the total number of months 
#simply count the number of months in the one column 
   
#Calculate the net total amount of profit/ losses over the entire period 

   
   
#simply add the columns up

#calculate the changes in Profit/ losses 

#calculate the average change based on the previous calculation 



#Find the greatest inclrease in profits 














#should Look like this 
#
  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
 # ```