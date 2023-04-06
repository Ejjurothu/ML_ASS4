import pandas as pd

# 1. Read the CSV file
df = pd.read_csv('data.csv')

# 2. Show basic statistical description
print(df.describe())

# 3. Check for null values and replace with mean
if df.isnull().values.any():
    df.fillna(df.mean(), inplace=True)

# 4. Aggregate using min, max, count, mean
agg_cols = ['Duration', 'Calories']
agg_funcs = ['min', 'max', 'count', 'mean']
agg_df = df[agg_cols].agg(agg_funcs)
print(agg_df)

# 5. Filter rows with calories between 500 and 1000
filtered_df1 = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print(filtered_df1)

# 6. Filter rows with calories > 500 and pulse < 100
filtered_df2 = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filtered_df2)

# 7. Create df_modified without Maxpulse column
df_modified = df.drop(columns=['Maxpulse'])

# 8. Delete Maxpulse column from df
df.drop(columns=['Maxpulse'], inplace=True)

# 9. Convert Calories column to int datatype
df['Calories'] = df['Calories'].astype(int)

# 10. Create a scatter plot for Duration and Calories
import matplotlib.pyplot as plt
df.plot.scatter(x='Duration', y='Calories')
plt.show()
