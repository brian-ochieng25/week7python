import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Set Seaborn style
sns.set(style="whitegrid")

# 1. Line Chart - Simulated sales data over time
dates = pd.date_range(start="2023-01-01", periods=12, freq='M')
sales = [200, 220, 250, 270, 300, 320, 310, 330, 350, 360, 380, 400]
df_sales = pd.DataFrame({'Date': dates, 'Sales': sales})

plt.figure(figsize=(10, 5))
plt.plot(df_sales['Date'], df_sales['Sales'], marker='o', linestyle='-', color='blue', label='Monthly Sales')
plt.title('Monthly Sales Trend in 2023')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average petal length per species in the Iris dataset
iris = sns.load_dataset("iris")
avg_petal_length = iris.groupby('species')['petal_length'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_petal_length, x='species', y='petal_length', palette='Set2')
plt.title('Average Petal Length per Iris Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.tight_layout()
plt.show()

# 3. Histogram - Distribution of sepal length
plt.figure(figsize=(8, 5))
sns.histplot(iris['sepal_length'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal length vs. Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species', palette='deep')
plt.title('Sepal Length vs Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()
