import pandas as pd
#Load data
df = pd.read_csv("C:\\Users\\hp\\Desktop\\zomato_data.csv",encoding='utf-8')
print("\nSAMPLE DATA SET")
#print(df)

# for understanding the data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

#clean column name
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)


