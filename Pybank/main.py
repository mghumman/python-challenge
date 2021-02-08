import csv
from math import * 
with open('dataset.csv') as r:
    string = csv.reader(r, delimiter = ',')
    next(string)
    months = 0 #stating the variables
    total = 0
    each = []
    rows = []
    for row in string:
        months += 1
        each.append(int(row[1])) #months list
        total += int(row[1])
        rows.append(row[0])#rows list
    profit_losses = 0
    #print(rows) to check if number of rows were correct
    changes = []
    for i in range(0,len(each)-1): #for loop
        changes.append(each[i+1] - each[i]) #adds dif of numbers to list
    #print(changes)
    #print(len(changes))
        
    #print('{}: {}'.format(months,total)) it was to check if the months and totals were printing out correctly
    print('Financial Analysis')
    print('________________________')
    print('Total Months:', months)
    print('Total:',total)
    print('Average Change:',sum(changes) / len(changes))
    
    
#used zybook for list and append functions and sum functions
increase = changes.index(max(changes))
greatest_increase = rows[decrease+1]
print ('Greatest increase in increase: {} ({})'.format(rows[increase+1],min(changes)))

decrease = changes.index(min(changes))
greatest_decrease = rows[decrease+1]
print ('Greatest decrease in profits: {} ({})'.format(rows[decrease+1],max(changes)))
