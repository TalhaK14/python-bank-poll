#!/usr/bin/env python
# coding: utf-8

# In[44]:


import os
import csv


# In[45]:


bank_csv= os.path.join('..', 'Downloads', 'Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
bank_csv


# In[69]:


total_months = []
net_total = []
monthly_change = []

with open(bank_csv, 'r') as csvfile:
 
    csvreader = csv.reader(csvfile,delimiter=",")

    header = next(csvreader)  

    for row in csvreader: 

        total_months.append(row[0])
        net_total.append(int(row[1]))

    for i in range(len(net_total)-1):
        
        monthly_change.append(net_total[i+1]-net_total[i])
        
max_value = max(monthly_change)
min_value = min(monthly_change)

max_month = monthly_change.index(max(monthly_change)) + 1
min_month = monthly_change.index(min(monthly_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_month]} (${(str(max_value))})")
print(f"Greatest Decrease in Profits: {total_months[min_month]} (${(str(min_value))})")


# In[ ]:





# In[ ]:




