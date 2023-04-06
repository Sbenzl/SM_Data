# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:04:14 2023

@author: SKYEBENSEL
"""
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Load data as columns 
column_subset = [
    "Date",
    "Site",
    "Arm",
    "Distance",
    "Soil",
    "SnowDepth",
    "CanopyCover",
    "theta"
    ]
df = pd.read_csv(r"C:\Users\skyebensel\Documents\Book1.csv", usecols=column_subset)

# drop all rows that have NaN/None values
df2=df.dropna()
print(df2)


#Group data by days
# group_day = df2.groupby('Date')['Soil'].mean()
# print(group_day)
x= df['Date']
y = df['Soil']

# plt.plot(x,y)
# plt.show
plt.figure(figsize=(10,6))
ax = sns.boxplot(x=x, y = y, data=df)
plt.xlabel('Date')

plt.ylabel('Soil Moisture (%)')
plt.title('Boxplot of Soil Moisture per Day')


plt.show()

# group1 = df[df["Soil"] == 'group1']["Distance"]
# group2 = df[df["SnowDepth"] == 'group2'["Dsitance"]]
# t_statistic, p_value = stats.ttest_ind(group1, group2)

