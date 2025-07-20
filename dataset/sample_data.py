import pandas as pd

df = pd.read_csv("dataset/zomato_data_cleaned.csv")
df.sample(20).to_csv("dataset/zomato_data_sample.csv", index=False)
