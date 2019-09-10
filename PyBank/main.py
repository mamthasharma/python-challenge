#import modules

import os
import csv

#define path to the csv

csvpath = os.path.join('budget_data.csv')
output_path = os.path.join("new.csv")
count_col=0
sum_col =0
max_profit = 0
max_loss = 0
row_counter =0
change_amt =0
next_amt =0
avg_change =0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader, None) 
    for row in csvreader:
        count_col+=1
        sum_col = sum_col+int(row[1])
        if row_counter>0:
           change_amt= (int(row[1])-next_amt)
           avg_change = change_amt+avg_change
           next_amt=int(row[1])
        else:
            next_amt = int(row[1])   
        row_counter += 1
        if max_profit < int(row[1]):
            max_profit = int(row[1])
       
        if max_loss>int(row[1]):
            max_loss = int(row[1])
avg_change = (avg_change/(row_counter-1))
    #print the values to terminal
    
print("Financial Analysis")
print("------------------------------------")
print(f"Total months: {count_col}")  
print(f"Total: {sum_col}")
print(f"Average change : {avg_change}")
print (f"Greatest increase in profits was in {row[0]} {max_profit}")
print (f"Greatest decrease in profits was in {row[0]} {max_loss}")

    # Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------------"])
    csvwriter.writerow(["Total months:", count_col])
    csvwriter.writerow(["Total :", sum_col])
    csvwriter.writerow(["Average change :", avg_change])
    csvwriter.writerow(["Greatest increase in profits :", row[0], max_profit])
    csvwriter.writerow(["Greatest decrease in profits :", row[0], max_loss])
          