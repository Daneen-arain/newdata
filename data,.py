import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "country": ["India", "USA", "Brazil", "India", "USA", np.nan, "Brazil", "India", "USA", "Brazil"],
    "date": ["1/1/2021", "1/1/2021", "1/1/2021", "1/2/2021", "1/2/2021", "1/2/2021", "1/3/2021", "1/3/2021", "1/3/2021", "1/4/2021"],
    "vaccines": ["Covaxin", "Pfizer", "CoronaVac", np.nan, "Moderna", "Pfizer", "CoronaVac", "Covaxin", np.nan, "CoronaVac"],
    "total_vaccinations": [1000, 2000, 1500, 1200, np.nan, 2500, 1800, np.nan, 2100, np.nan],
    "people_vaccinated": [800, 1800, 1400, 1100, 1700, np.nan, np.nan, 1000, 1900, 1600],
    "people_fully_vaccinated": [200, 200, 100, np.nan, 200, 300, 400, 200, np.nan, 300]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nNull values per column:")
print(df.isnull().sum())

# Step 6: Visualize missing data
sns.heatmap(df.isnull(), cbar=False, cmap="magma")
plt.title("Missing Data Heatmap")
plt.show()

df = df.dropna(how="all")

df["country"] = df["country"].fillna("Unknown")
df["vaccines"] = df["vaccines"].fillna("Unknown")
df["total_vaccinations"] = df["total_vaccinations"].fillna(method="ffill")
df["people_vaccinated"] = df["people_vaccinated"].fillna(method="bfill")
df["people_fully_vaccinated"] = df["people_fully_vaccinated"].fillna(0)

# Step 8: View cleaned data
print("\nCleaned Data:")
print(df)
