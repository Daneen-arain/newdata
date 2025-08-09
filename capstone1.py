import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Better style
sns.set(style="whitegrid")

# --- DATA ---
data = {
    "Species": ["Adelie"] * 21,
    "Island": ["Dream"] * 18 + ["Biscoe"] * 3,
    "Bill Length (mm)": [37.3, 41.3, 36.3, 36.9, 38.3, 38.9, 35.7, 41.1, 34.0, 39.6,
                         36.2, 40.8, 38.1, 40.3, 33.1, 43.2, 35.0, 41.0, 37.7],
    "Bill Depth (mm)": [17.8, 20.3, 19.5, 18.6, 19.2, 18.8, 18.0, 18.1, 17.1, 18.1,
                        17.3, 18.9, 18.6, 18.5, 16.1, 18.5, 17.9, 20.0, 16.0],
    "Flipper Length (mm)": [191, 194, 190, 189, 189, 190, 202, 205, 185, 186,
                            187, 208, 190, 196, 178, 192, 192, 203, 183],
    "Body Mass (g)": [3350, 3550, 3800, 3500, 3950, 3600, 3550, 4300, 3400, 4450,
                      3300, 4300, 3700, 4350, 2900, 4100, 3725, 4725, 3075],
    "Sex": ["FEMALE", "MALE", "MALE", "FEMALE", "MALE", "FEMALE", "FEMALE", "MALE",
            "FEMALE", "MALE", "FEMALE", "MALE", "FEMALE", "MALE", "FEMALE", "MALE",
            "FEMALE", "MALE", "FEMALE"]
}

df = pd.DataFrame(data)

# --- 1. Count Plot of Sex ---
sns.countplot(x='Sex', data=df)
plt.title("Count of Penguins by Sex")
plt.show()

# --- 2. Histogram of Body Mass ---
plt.hist(df["Body Mass (g)"], bins=6, color='skyblue')
plt.title("Distribution of Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Count")
plt.show()

# --- 3. Box Plot: Flipper Length by Sex ---
sns.boxplot(x="Sex", y="Flipper Length (mm)", data=df)
plt.title("Flipper Length by Sex")
plt.show()

# --- 4. Violin Plot: Bill Depth by Sex ---
sns.violinplot(x="Sex", y="Bill Depth (mm)", data=df)
plt.title("Bill Depth by Sex")
plt.show()

# --- 5. Scatter Plot: Bill Length vs Body Mass ---
sns.scatterplot(x="Bill Length (mm)", y="Body Mass (g)", hue="Sex", data=df)
plt.title("Bill Length vs Body Mass")
plt.show()

# --- 6. Pairplot of All Numeric Features ---
sns.pairplot(df, hue="Sex")
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()

# --- 7. Bar Plot: Avg Body Mass by Island ---
sns.barplot(x="Island", y="Body Mass (g)", data=df)
plt.title("Average Body Mass by Island")
plt.show()

# --- 8. Heatmap of Correlations ---
corr = df.drop(["Species", "Island", "Sex"], axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# --- 9. Swarm Plot: Flipper Length by Sex ---
sns.swarmplot(x="Sex", y="Flipper Length (mm)", data=df)
plt.title("Flipper Length Distribution by Sex")
plt.show()

# --- 10. KDE Plot: Body Mass by Sex ---
sns.kdeplot(data=df, x="Body Mass (g)", hue="Sex", fill=True)
plt.title("Body Mass Distribution by Sex")
plt.show()
