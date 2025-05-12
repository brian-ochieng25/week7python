import pandas as pd

# Step 1: Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore structure - data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Clean the dataset (fill or drop missing values)


# Option A: Drop rows with missing values
df_cleaned = df.dropna()

# Option B: Fill missing values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))

print("\nData cleaned successfully.")