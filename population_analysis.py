import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv', skiprows=4)

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst few rows:")
print(df.head())

# Filter for India
india_data = df[df['Country Name'] == 'India']

# Get population data for India from 1960 to 2024
years = [col for col in df.columns if col.isdigit() and 1960 <= int(col) <= 2024]
india_population = india_data[years].iloc[0]

# Create a DataFrame for plotting
plot_df = pd.DataFrame({
    'Year': [int(year) for year in years],
    'Population': india_population.values
})

# Plot India's population over time
plt.figure(figsize=(12, 6))
plt.plot(plot_df['Year'], plot_df['Population'] / 1e6, marker='o', linewidth=2)
plt.title('India Population Growth (1960-2024)')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True, alpha=0.3)
plt.xticks(range(1960, 2025, 5), rotation=45)
plt.tight_layout()
plt.show()

# Get the most recent data (2022-2024)
recent_years = ['2022', '2023', '2024']
recent_data = india_data[recent_years].iloc[0]
print("\nIndia's recent population:")
for year, pop in zip(recent_years, recent_data):
    print(f"{year}: {pop:,}")

# Create age group analysis (simulated based on typical population structure)
# This is a simplified representation since the dataset doesn't have age breakdowns
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']
# Typical age distribution for India (approximate percentages)
age_percentages = [26.2, 17.9, 41.1, 8.9, 5.9]  # Based on demographic data

# Create age distribution plot for 2022
population_2022 = int(india_data['2022'].iloc[0])
age_populations = [population_2022 * (p/100) for p in age_percentages]

plt.figure(figsize=(10, 6))
plt.bar(age_groups, [p/1e6 for p in age_populations], color=['skyblue', 'lightgreen', 'orange', 'lightcoral', 'gold'])
plt.title('India Population by Age Group (2022)')
plt.xlabel('Age Group')
plt.ylabel('Population (millions)')
plt.grid(True, alpha=0.3)
for i, (group, pop) in enumerate(zip(age_groups, age_populations)):
    plt.text(i, pop/1e6 + 5, f'{pop/1e6:.1f}M', ha='center', va='bottom')
plt.tight_layout()
plt.show()

print("\nAnalysis complete! The plots show:")
print("1. India's population growth from 1960-2024")
print("2. Age group distribution for 2022 (simulated based on demographic patterns)")
print(f"3. India's population in 2022: {population_2022:,}")
