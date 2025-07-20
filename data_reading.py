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




