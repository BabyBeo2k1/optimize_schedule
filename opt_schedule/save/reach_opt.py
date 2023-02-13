import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
data = {'N': [10, 50, 100, 150, 200],
        'Dynamic Programming': [100, 100, 100, 100, 100],
        'Heuristic': [70, 65, 35, 45, 50],
        'Genetic Algorithm': [90, 85, 10, 0, 0],
        'Hill Climbing': [35, 10, 0, 0, 0],
        'IP': [100, 100, 100, 100, 100],
        'Brute force': [95, 35, 10, 25, 20]}
df = pd.DataFrame(data)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 7))
df.set_index('N').plot.bar(ax=ax)

# Add title and axis labels
ax.set_title("Ability to reach optimal solution comparison", fontsize=20)
ax.set_xlabel("N", fontsize=16)
ax.set_ylabel("Rate(%)", fontsize=16)

# Set the x-axis labels to be horizontal
ax.set_xticklabels(df['N'], rotation=0)

# Increase the size of the legend
ax.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
if __name__ == "__main__":
    # Show the plot
    plt.show()