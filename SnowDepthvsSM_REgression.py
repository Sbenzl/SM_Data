# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 12:47:39 2023

@author: SKYEBENSEL
"""

import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Load data
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
df = pd.read_csv(r"C:\Users\skyebensel\.spyder-py3\Field_Hydrology/SM_Data.csv", usecols=column_subset, nrows=324)
# Normalize data

# drop all rows that have NaN/None values
df2=df.dropna()
print(df2)

# Define a function to compute R-squared value
def rsq(x, y, **kwargs):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    r_squared = r_value ** 2
    ax = plt.gca()
    ax.text(0.8, 0.2, f"R-squared = {r_squared:.2f}", transform=ax.transAxes, fontsize=14)

# Create a linear regression plot with R-squared values for each group
# sns.lmplot(x='SnowDepth', y='Soil', data=df2, hue='Date', col='Date', col_wrap=3, height=5, aspect=1.2, line_kws={'linewidth':1.5}, scatter_kws={'s': 50}, ci=None, truncate=True)
# g = sns.FacetGrid(df, col='Date', col_wrap=3, height=5, aspect=1.2)
# g.map(rsq, 'SnowDepth', 'Soil')


# Create a regression plot for each date
g = sns.lmplot(x="SnowDepth", y="Soil", col="Date", hue="Date", data=df2, ci=None)
g.map(rsq, 'SnowDepth', 'Soil')
# Set the axis labels
g.set_axis_labels("Snow Depth (cm)", "Soil Moisture (%)")

# Set the title for each plot
for ax in g.axes.flat:
    ax.set_title(ax.get_title().split("=")[-1])

# Combine the plots into a single figure
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Linear Regression of Snow Depth vs Soil Moisture by Date")

# Show the plot
plt.show()