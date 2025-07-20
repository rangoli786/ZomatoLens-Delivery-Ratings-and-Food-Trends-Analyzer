import pandas as pd
import numpy as np
#Load data
df = pd.read_csv("C:\\Users\\hp\\Desktop\\zomato_data.csv",encoding='utf-8')
print("\nSAMPLE DATA SET")
#print(df)

#clean column name
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
#drop duplicates
df.drop_duplicates(inplace=True)
#missing value treatement
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# Drop rows with critical missing values (e.g., Rating, Cuisine)
df.dropna(subset=['rating', 'cuisine', 'average_cost'], inplace=True)

# Fill less critical columns with default or common values
df['restaurant_type'] = df['restaurant_type'].fillna('Casual Dining')
df['delivery_time'] = df['delivery_time'].fillna(df['delivery_time'].median())

#fix data type
# Remove currency symbols and convert to numeric
df['average_cost'] = df['average_cost'].astype(str).str.replace('[₹,]', '', regex=True)
df['average_cost'] = pd.to_numeric(df['average_cost'], errors='coerce')

# Votes may have commas (e.g., 1,234) – fix that
df['votes'] = df['votes'].astype(str).str.replace(',', '')
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')
#standardize categorical values
df['online_order'] = df['online_order'].str.lower().map({'yes': 'Yes', 'no': 'No', 'yes ': 'Yes', 'no ': 'No'})

df['book_table'] = df['book_table'].str.strip().str.capitalize()

df['cuisine'] = df['cuisine'].str.strip().str.title()
#remove outliers
# Remove restaurants with extremely high delivery times or cost
df = df[df['delivery_time'] < 90]
df = df[df['average_cost'] < 5000]
# Add price category
df['cost_category'] = pd.cut(df['average_cost'],
                              bins=[0, 200, 500, 1000, np.inf],
                              labels=['Budget', 'Moderate', 'Premium', 'Luxury'])

# Extract primary cuisine if multiple cuisines listed
df['primary_cuisine'] = df['cuisine'].apply(lambda x: x.split(',')[0])
print(df.info())
print(df.describe())



import os

# Create 'dataset' folder if it doesn't exist
os.makedirs("dataset", exist_ok=True)

# Now save the cleaned CSV
df.to_csv("dataset/zomato_data_cleaned.csv", index=False)



