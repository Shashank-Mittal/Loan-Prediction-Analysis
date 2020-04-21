
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib as plt

# In[2]:

df=pd.read_csv("Dataset//train_ctrUa4K.csv") #To Read the Dataset
print("hello")


# In[3]:


df.head(10) # Show 10 rows of the data


# In[4]:


df.describe() #Discription of the data


# In[5]:


df['Property_Area'].value_counts() #To get the count with Clusters in Property_Area 


# In[8]:


df['ApplicantIncome'].hist(bins=50) #Histogram of ApplicantIncome
df.boxplot(column='ApplicantIncome' ,by='Education')
