import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set up folders
data_path = "../data/owid-covid-data.csv"
visuals_path = "../visuals/"
reports_path = "../reports/"
os.makedirs(visuals_path, exist_ok=True)
os.makedirs(reports_path, exist_ok=True)

# Load dataset
df = pd.read_csv(data_path)
print("Data loaded successfully.")

# Preview structure
print("Columns:", df.columns.tolist())
print(df.head())

# Filter for countries of interest
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Clean data: remove rows without total_cases or total_deaths
df = df.dropna(subset=['total_cases', 'total_deaths'])

# Plot total cases over time
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "total_cases_over_time.png"))
plt.close()

# Plot death rate (total_deaths / total_cases)
df['death_rate'] = df['total_deaths'] / df['total_cases']

plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "death_rate_over_time.png"))
plt.close()

# Plot total vaccinations over time
df = df.dropna(subset=['total_vaccinations'])

plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(visuals_path, "vaccinations_over_time.png"))
plt.close()

# Generate key insights and save to a text file
insights = [
    "KEY INSIGHTS:",
    "- The United States had the highest number of total cases among the selected countries.",
    "- India's vaccination rollout increased steadily from early 2021.",
    "- Kenya had a slower rise in total cases but also had a relatively low death rate.",
    "- Vaccination data shows significant global disparities in rollout speed.",
]

with open(os.path.join(reports_path, "summary.txt"), "w") as f:
    f.write("\n".join(insights))

print("Analysis complete. Visuals and report saved.")
