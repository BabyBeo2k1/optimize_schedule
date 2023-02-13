import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
data = {'N': [10, 50, 100, 150, 200],
        'Dynamic Programming': [100, 100, 100, 100, 100],
        'Heuristic': [97, 95, 92, 95, 97],
        'Genetic Algorithm': [99, 99, 86, 53, 23],
        'Hill Climbing': [68, 42, 19, 27, 25],
        'IP': [100, 100, 100, 100, 100],
        'Brute force': [99, 97, 67, 63, 58]}
df = pd.DataFrame(data)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 7))
df.set_index('N').plot.bar(ax=ax)

# Add title and axis labels
ax.set_title("Ability to approximate optimal solution comparison", fontsize=20)
ax.set_xlabel("N", fontsize=16)
ax.set_ylabel("Approximation(%)", fontsize=16)

# Set the x-axis labels to be horizontal
ax.set_xticklabels(df['N'], rotation=0)

# Increase the size of the legend
ax.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
if __name__ == "__main__":
    # Show the plot
    plt.show()