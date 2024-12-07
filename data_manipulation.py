import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ml.csv")

# print(df.head())
# print(df.describe())
# print(df.shape)

# # Display unique values for categorical columns
# categorical_columns = df.select_dtypes(include=["object"]).columns
# for col in categorical_columns:
#     unique_values = df[col].unique()
#     print(f"{col}: {len(unique_values)} unique values")

# # value counts
# for col in df.columns:
#     print(df['fuel_type'].value_counts())

# df.rename(columns={'fuel_type':'purchase_date'}, inplace=True)
# print(df)

# print(df.drop(['Unnamed: 0'], axis=1, inplace=True))
# print(df.head())

# print(df.isnull().sum())

# # Convert Data Types
# """errors parameter can contain {
#     raise: (default) raises an error for invalid parsing.
#     coerce: converts invalid parsing to NaN
#     ignore: returns the original data without any changes
#     } """
# df['selling_price'] = df['selling_price'].astype(float)
# df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
# df["purchase_price"] = pd.to_numeric(df["purchase_price"], errors="coerce", downcast="float")
# print(df.dtypes)

# plt.figure(figsize = (20, 5))
# sns.countplot(x='manufacturer', data=df.sort_values(by='manufacturer'), hue='manufacturer', palette='husl', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Companies with their sold Vehicles", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
# plt.show()

# plt.figure(figsize = (20, 5))
# sns.countplot(x='color', data=df.sort_values(by='color'), hue='color', palette='Spectral', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Distribution of Vehicles colors", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
# plt.show()

# # Assuming 'car_data' is your DataFrame and 'Year' is the column to count
# plt.figure(figsize=(20, 5))
# sns.countplot(x='year', data=df, hue='year', palette='dark', legend=False)  # Use 'x' for the column
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Number of vehicles manufactured in different years", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xlabel("Year", fontsize=15)  # Optional: Label for the x-axis
# plt.ylabel("Count", fontsize=15)  # Optional: Label for the y-axis
# plt.xticks(rotation=45)  # Optional: Rotate x labels for better visibility
# plt.show()

# plt.figure(figsize=(18, 6))
# sns.countplot(x='owner_age', data=df, hue='owner_age', palette='viridis', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Vehicle owners age", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
# plt.show()

# plt.figure(figsize = (20, 5))
# sns.countplot(x='owner_profession', data=df.sort_values(by='owner_profession'), hue='owner_profession', palette='colorblind', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Distribution of vehicles by owner profession", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
# plt.show()

# plt.figure(figsize = (20, 5))
# sns.countplot(x='fuel_type', data=df.sort_values(by='fuel_type'), hue='fuel_type', palette='Paired', legend=False)
# plt.grid(color="green", linestyle="--", linewidth=0.5)
# plt.title("Distribution of vehicles by their fuel type", fontdict={"family": "serif", "color": "blue", "size": 20})
# plt.xticks(rotation=90)  # Optional: Rotate x labels for better visibility
# plt.show()

# df.nunique()

df.groupby('manufacturer').agg({
    'seating_capacity': ['min', 'max', 'mean', 'std', 'first', 'last'],
    'selling_price': ['min', 'max', 'mean', 'std', 'sum'],
    'purchase_price': ['min', 'max', 'mean', 'std', 'sum']
})

plt.figure(figsize = (15, 4))
df.groupby('manufacturer')['purchase_price'].sum().plot(kind = 'pie', autopct='%1.1f%%', startangle=90, legend=False)
plt.title("The income in different manufacturers", fontsize = 20)
plt.show()
