#!/usr/bin/env python
# coding: utf-8

# In[7]:


import csv


# In[8]:


path = 'Resources/budget_data.csv'


# In[10]:


with open(path) as csvfile:
    
    reader = csv.reader(csvfile, delimiter =',')
    
    
    csv_header = next(reader)
    
    months = 0
    net = 0
    avg = 0
    max = 0
    min = 0
    
    for row in reader:
        months = months + 1
        value = int(row[1])
        net = net + value
        
        if value > max:
            max = value
        
        if value < min:
            min = value
        
    avg = net / months    
    avg = str(round(avg, 2))
    
    print('Financial Analysis')
    print('')
    print(f"Total Months: {months}")
    print(f"Total: ${net}")
    print(f"Average Change: ${avg}")
    print(f"Greatest Profit: ${max}")
    print(f"Greatest Loss: ${min}")


# In[11]:


output = 'Analysis/PyBankAnalysis.csv'


# In[14]:


with open(output, 'w', newline='') as csvfile:

  
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow([' '])
    csvwriter.writerow(['Total Months: 86'])
    csvwriter.writerow(['Total: $38382578'])
    csvwriter.writerow(['Average Change: $446309.05'])
    csvwriter.writerow(['Greatest Profit: $1170593'])
    csvwriter.writerow(['Greatest Loss: $-1196225'])

