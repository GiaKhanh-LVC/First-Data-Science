import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"D:/Heart-Disease-Dataset-first-Data-Science/main/heart.csv")

# Group the data by age and heart disease status (target)
# Assuming 'target' column indicates heart disease (1 = disease, 0 = no disease)
age_heart_disease = data.groupby(['age', 'target']).size().unstack(fill_value=0)

# Plotting the bar chart
ax=age_heart_disease.plot(kind='bar', figsize=(14, 7), color=['skyblue', 'salmon'])

# Add titles and labels
plt.title('Comparison of Age and Heart Disease')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')
plt.legend(['No Heart Disease', 'Heart Disease'], title='Condition')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
for i in ax.containers:
    ax.bar_label(i, label_type='edge', fontsize=10, color='black')
# Display the plot
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
