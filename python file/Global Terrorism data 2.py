#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os

file_path = r"C:\Users\saiya\Downloads\dataset\data-society-global-terrorism-data\gtd1993_748.csv"


data = pd.read_csv(file_path, encoding='latin1')
print(data.head())


# In[2]:


# 1. Remove irrelevant columns
# Assuming columns like 'addnotes', 'scite1', 'scite2', 'scite3', and others unrelated to analysis can be dropped
irrelevant_columns = ['addnotes', 'scite1', 'scite2', 'scite3', 'dbsource']
data_cleaned = data.drop(columns=irrelevant_columns, errors='ignore')

data_cleaned.head()


# In[3]:


# Replace missing values in numerical columns with 0 and categorical columns with 'Unknown'
numerical_columns = data_cleaned.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = data_cleaned.select_dtypes(include=['object']).columns
data_cleaned[numerical_columns] = data_cleaned[numerical_columns].fillna(0)
data_cleaned[categorical_columns] = data_cleaned[categorical_columns].fillna('Unknown')
data_cleaned.columns = data_cleaned.columns.str.strip().str.lower().str.replace(' ', '_')

data_cleaned.head()


# In[4]:


data_cleaned = data_cleaned.drop_duplicates()

data_cleaned.head()


# In[5]:


data_cleaned = data_cleaned[data_cleaned['iyear'] == 1993]


# In[6]:


# data_cleaned.to_csv(r"C:\Users\saiya\Downloads\dataset\data-society-global-terrorism-data\cleaned dataset", index=False)
data_summary = {
    "Shape": data_cleaned.shape,
    "Missing Values": data_cleaned.isnull().sum().sum(),
    "Preview": data_cleaned.head()
}

data_summary


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


sns.set_theme(style="whitegrid")


# In[9]:


# 1. Trend Analysis
def trend_analysis(data):
    trend_data = data['iyear'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=trend_data.index, y=trend_data.values, marker="o")
    plt.title("Number of Terrorist Incidents per Year", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Number of Incidents", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(visible=True)
    plt.show()


# In[10]:


# 2. Geographical Insights
def geographical_insights(data):
    region_data = data['region'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=region_data.index, y=region_data.values, palette="viridis")
    plt.title("Top Regions Affected by Terrorism", fontsize=16)
    plt.xlabel("Region", fontsize=14)
    plt.ylabel("Number of Incidents", fontsize=14)
    plt.xticks(rotation=45)
    plt.show()


# In[11]:


# 3. Attack Types and Targets
def attack_types_and_targets(data):
    attack_data = data['attacktype1_txt'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(y=attack_data.index, x=attack_data.values, palette="rocket")
    plt.title("Most Common Types of Attacks", fontsize=16)
    plt.xlabel("Number of Incidents", fontsize=14)
    plt.ylabel("Attack Type", fontsize=14)
    plt.show()
    
    
    
    target_data = data['targtype1_txt'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(y=target_data.index, x=target_data.values, palette="mako")
    plt.title("Most Common Targets of Attacks", fontsize=16)
    plt.xlabel("Number of Incidents", fontsize=14)
    plt.ylabel("Target Type", fontsize=14)
    plt.show()



# In[12]:


# 4. Perpetrator Analysis
def perpetrator_analysis(data):
    group_data = data['gname'].value_counts().head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(y=group_data.index, x=group_data.values, palette="coolwarm")
    plt.title("Top 10 Perpetrator Groups", fontsize=16)
    plt.xlabel("Number of Incidents", fontsize=14)
    plt.ylabel("Group Name", fontsize=14)
    plt.show()


# In[13]:


# 5. Casualty and Impact Analysis
def casualty_analysis(data):
    data['total_casualties'] = data['nkill'] + data['nwound']
    casualty_data = data[['iyear', 'total_casualties']].groupby('iyear').sum()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=casualty_data.index, y=casualty_data['total_casualties'], marker="o", color="red")
    plt.title("Total Casualties Over the Years", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Total Casualties", fontsize=14)
    plt.grid(visible=True)
    plt.show()
    
        # Incidents with the highest casualties
    top_casualties = data[['eventid', 'iyear', 'nkill', 'nwound', 'total_casualties']].nlargest(10, 'total_casualties')
    print("Top 10 Incidents with Highest Casualties:")
    print(top_casualties)


# In[14]:


# Run the analysis
trend_analysis(data)
geographical_insights(data)
attack_types_and_targets(data)
perpetrator_analysis(data)
casualty_analysis(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




