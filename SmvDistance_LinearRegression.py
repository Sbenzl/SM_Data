# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Load data
column_subset = [
    "Date",
    "Distance",
    "Moisture"]
df = pd.read_csv(r"C:/Users/skyebensel/.spyder-py3/Field_Hydrology/SM_Distance.csv", usecols=column_subset, nrows=324)
# Normalize data

# drop all rows that have NaN/None values
df2=df.dropna()
print(df2)

# Plot data with linear regression and R-squared value
sns.lmplot(x='Distance', y='Moisture', hue='Date', data=df, height=6, aspect=1.5)

#mask = ~np.isnan(x)  #masked NaN values



# Calculate and display R-squared value for each group
groups = df2.groupby('Date')

for name, group in groups:
    slope, intercept, r_value, p_value, std_err = stats.linregress(group['Distance'], group['Moisture'])
    r_squared = r_value ** 2
    plt.text(1, group['Moisture'].mean(), f"R-squared = {r_squared:.3f}", fontsize=12)
   


# Set x-axis tick labels
plt.xticks([i/2 for i in range(0, 15)])

plt.xlim(-0.005, 1.6)
plt.ylim(0, 50)
plt.xlabel('Distance from Sagebrush (m)')
plt.ylabel('Soil Moisture (%)')
plt.title('Linear Regression')

# Show plot
plt.show()
