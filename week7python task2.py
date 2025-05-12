import pandas as pd

# Step 1: Load Data
df = pd.read_csv("your_dataset.csv")  # Replace with your actual file path

# Step 2: Basic Statistics
print("Basic statistics:\n", df.describe())

# Step 3: Group by a Categorical Column and Compute Mean

grouped_mean = df.groupby("species")["weight"].mean()
print("\nMean weight by species:\n", grouped_mean)

# Step 4: Identify Patterns or Insights

sorted_means = grouped_mean.sort_values(ascending=False)
print("\nSorted mean weight by species:\n", sorted_means)

# Optional: Visualize
import matplotlib.pyplot as plt
sorted_means.plot(kind='bar', title='Average Weight by Species')
plt.ylabel("Average Weight")
plt.tight_layout()
plt.show()