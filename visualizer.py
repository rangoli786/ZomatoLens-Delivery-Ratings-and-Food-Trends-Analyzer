"""
DATA ANALYSIS
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/zomato_data_cleaned.csv")

 #Clean column names
df.columns = df.columns.astype(str)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_', regex=True)

# Set Seaborn plot style
sns.set(style="whitegrid")

# Cuisine Popularity
top_cuisines = df['cuisine'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette="viridis")
plt.title("Top 10 Most Common Cuisines")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig("plot1_cuisine_popularity.png")
plt.clf()

# Cost vs Rating
sns.scatterplot(data=df, x='average_cost', y='rating', hue='online_order', palette='Set1', alpha=0.7)
plt.title("Average Cost vs Rating with Online Order")
plt.xlabel("Average Cost (₹)")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("plot2_cost_vs_rating.png")
plt.clf()

# Delivery Time Histogram
sns.histplot(df['delivery_time'], bins=20, kde=True, color='skyblue')
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("plot3_delivery_time_hist.png")
plt.clf()

# Votes vs Rating
sns.scatterplot(data=df, x='votes', y='rating', alpha=0.6, color='orange')
plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("plot4_votes_vs_rating.png")
plt.clf()

# Restaurant Type Distribution
rest_type_counts = df['restaurant_type'].value_counts().head(10)
sns.barplot(x=rest_type_counts.values, y=rest_type_counts.index, palette="cubehelix")
plt.title("Top 10 Restaurant Types")
plt.xlabel("Count")
plt.ylabel("Restaurant Type")
plt.tight_layout()
plt.savefig("plot5_restaurant_types.png")
plt.clf()

print("All plots saved as PNG files.")
print(df.columns)