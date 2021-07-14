#!/usr/bin/env python
# coding: utf-8

# In[39]:


import csv


# In[40]:


path = 'Resources/election_data.csv'


# In[41]:


with open(path) as csvfile:
    
    reader = csv.reader(csvfile, delimiter =',')
    
    csv_header = next(reader)
        
    votes = 0
    Khan = 0
    K_per = 0
    Correy = 0
    C_per = 0
    Li = 0
    L_per = 0
    O_Tooley = 0
    O_per = 0
    
    Winner = []
    
    for row in reader:
        votes = votes + 1
        
        if row[2] == 'Khan':
            Khan = Khan + 1
        elif row[2] == 'Correy':
            Correy = Correy + 1
        elif row[2] == 'Li':
            Li = Li + 1
        elif row[2] == "O'Tooley":
            O_Tooley = O_Tooley + 1
        else:
            print(row)
            
    K_per = Khan / votes
    C_per = Correy / votes
    L_per = Li / votes
    O_per = O_Tooley / votes
    
    


# In[42]:


if Khan > Correy:
        if Khan > Li:
            if Khan > O_Tooley:
                Winner = 'Khan'
            else:
                Winner = "O'Tooley"
        elif Li > Khan:
            if Li > O_Tooley:
                Winner = 'Li'
            else:
                Winner = "O'Tooley"
else:
    if Correy > Li:
            if Correy > O_Tooley:
                Winner = 'Correy'
            else:
                Winner = "O'Tooley"
    elif Li > Correy:
        if Li > O_Tooley:
            Winner = 'Li'
        else:
            Winner = "O'Tooley"
    
                


# In[48]:


print('--------------------------')
print('Election Results')
print('--------------------------')
print(f"Total Votes: {votes}")
print('--------------------------')
print(f"Khan: {K_per} ({Khan})")
print(f"Correy: {C_per} ({Correy})")
print(f"Li: {L_per} ({Li})")
print(f"O'Tooley: {O_per} ({O_Tooley})")
print('--------------------------')
print(f'Winner: {Winner}')
print('--------------------------')


# In[50]:


output = 'Analysis/PyPollAnalysis.csv'


# In[52]:


with open(output, 'w', newline='') as csvfile:

  
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Election Analysis'])
    csvwriter.writerow([' '])
    csvwriter.writerow(['Khan: 0.6300001050837531 (2218231)'])
    csvwriter.writerow(['Correy: 0.19999994319797126 (704200)'])
    csvwriter.writerow(['Li: 0.13999996023857988 (492940)'])
    csvwriter.writerow(["O'Tooley: 0.02999999147969569 (105630)"])
    csvwriter.writerow(['Winner: Khan'])

