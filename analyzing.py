"""
DATA ANALYSING
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("dataset/zomato_data_cleaned.csv")
#print(df)
#(A)----------------------------------------------------------------------------------------------------------
# Extracting high rating dishes
top_rated_dishes = df.sort_values('rating',ascending=False).head(10)
print("\nTOP RATED DISHES/CUISINE")
print(top_rated_dishes[['primary_cuisine','rating','name','cost_category','restaurant_type']])
#(B)------------------------------------------------------------------------------------------------------------------------------------------
# for tracking order type
#  1. Value counts for order methods
print("\n Online Order Availability:")
print(df['online_order'].value_counts())
print("\n Table Booking Availability:")
print(df['book_table'].value_counts())
#  2. Average rating comparison
print("\n Average Rating Based on Online Ordering:")
print(df.groupby('online_order')['rating'].mean().round(2))
print("\n Average Rating Based on Table Booking:")
print(df.groupby('book_table')['rating'].mean().round(2))
#  3. Crosstab: Online Order vs Table Booking
print("\n Crosstab of Online Order and Table Booking:")
print(pd.crosstab(df['online_order'], df['book_table']))
#  4. Most common combinations
print("\nMost Common Order Combinations:")
print(df.groupby(['online_order', 'book_table']).size().sort_values(ascending=False))
#(C)------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Most common delivery time 
Make sure delivery_time is numeric

Label the delivery times
"""
def label_delivery_time(time):
    if pd.isna(time):
        return 'Unknown'
    elif time <= 70:
        return 'Fast (≤70 mins)'
    elif time <= 79:
        return 'Moderate (71-80 mins)'
    else:
        return 'Slow (80+ mins)'

df['delivery_label'] = df['delivery_time'].apply(label_delivery_time)
print(df[['delivery_time', 'delivery_label']].head())
print(df[['delivery_time', 'delivery_label']].tail())
#(D)----------------------------------------------------------------------
#average delivery time
print("Average Delivery Time:", df['delivery_time'].mean(), "minutes")





