import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset as per the earlier structure
data = pd.DataFrame({
    "Country": ["India", "USA", "China", "Germany"],
    "Property Rights": [60, 85, 40, 80],
    "Government Integrity": [55, 80, 45, 75],
    "Tax Burden": [80, 65, 90, 60],
    "Trade Freedom": [70, 90, 65, 85],
    "Investment Freedom": [65, 85, 60, 80],
    "Financial Freedom": [58, 88, 55, 83]
})

# Calculate the Freedom Index
freedom_columns = data.columns[1:]
data['Freedom Index'] = data[freedom_columns].mean(axis=1)

# Sort data by Freedom Index
sorted_data = data.sort_values(by="Freedom Index", ascending=False)

# Plot the bar chart
plt.figure(figsize=(10, 5))
sns.barplot(x="Country", y="Freedom Index", data=sorted_data, palette="viridis")
plt.title("Economic Freedom Index by Country")
plt.ylabel("Freedom Index (0-100)")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display the resulting DataFrame
sorted_data.reset_index(drop=True)