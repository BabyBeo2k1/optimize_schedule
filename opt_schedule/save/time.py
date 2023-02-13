import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
data = {'N': [10, 50, 100, 150, 200],
        'Dynamic Programming': [0.2926, 1.8390, 3.2076, 5.1726, 5.3132],
        'Heuristic': [0.0010, 0.0019, 0.0051, 0.0097, 0.0135],
        'Genetic Algorithm': [24.0032, 44.3138, 67.8872, 95.1432, 121.1749],
        'Hill Climbing': [0.1499, 0.3348, 0.6215, 0.9220, 1.1385],
        'IP': [0.0047, 0.0107, 0.0174, 0.0298, 0.0341],
        'Brute force': [60.3491, 227.5745, 270.2315, 254.1159, 270.0061]}
df = pd.DataFrame(data)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 7))
df.set_index('N').plot.bar(ax=ax)

# Add title and axis labels
ax.set_title("Run time comparison", fontsize=20)
ax.set_xlabel("N", fontsize=16)
ax.set_ylabel("Time(s)", fontsize=16)

# Set the x-axis labels to be horizontal
ax.set_xticklabels(df['N'], rotation=0)

# Increase the size of the legend
ax.legend(fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
if __name__ == "__main__":
    # Show the plot
    plt.show()