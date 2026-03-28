# Obesity–Depression Gene Expression Analysis

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Creating a dataset related to obesity and depression
data = {
    'Gene': ['TNF', 'IL6', 'LEP', 'BDNF', 'INS', 'CRP'],
    'Expression_Level': [8.5, 7.8, 6.2, 4.5, 5.0, 7.2],
    'Condition': ['Obesity+Depression', 'Obesity+Depression', 'Obesity',
                  'Depression', 'Normal', 'Obesity+Depression']
}

# Convert to DataFrame
gene_data = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(gene_data)

# Basic statistics
print("\nStatistical Summary:")
print(gene_data.describe())

# Group by condition and calculate mean expression
expression_summary = gene_data.groupby('Condition')['Expression_Level'].mean()
print("\nAverage Expression by Condition:")
print(expression_summary)

# Plotting the results
expression_summary.plot(kind='bar')
plt.title("Gene Expression in Obesity–Depression Comorbidity")
plt.xlabel("Condition")
plt.ylabel("Expression Level")
plt.show()