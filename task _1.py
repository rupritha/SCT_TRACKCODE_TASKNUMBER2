import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('india_age_distribution_2022.csv')

# Filter for 2022 and aggregate by age group (ignoring gender breakdown for now)
df_2022 = df[(df['year'] == 2022) & (df['gender'] == 'Person')]

# Make sure your column names match exactly (case and whitespace sensitive)
age_groups = df_2022['age_group']
percentages = df_2022['value']

# Plot
plt.figure(figsize=(10, 6))
plt.bar(age_groups, percentages, color='skyblue')
plt.title("India Population Distribution by Age Group (2022)")
plt.xlabel("Age Group")
plt.ylabel("Percentage of Total Population (%)")
plt.xticks(rotation=45)
plt.tight_layout()

# Show value labels
for i, v in enumerate(percentages):
    plt.text(i, v + 0.2, f"{v}%", ha='center', fontsize=10)

plt.show()
