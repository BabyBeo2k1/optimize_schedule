import matplotlib.pyplot as plt
import pickle


range_N = [10, 50, 100, 150, 200]
range_change = [2, 4, 8]
hill_climbing_file = []
for i in range_change:
    hill_climbing_file.append([f"record_{N}_{i}.pickle" for N in range_N])


# Create the figure and the subplots
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 10), gridspec_kw={'width_ratios': [1, 1], 'height_ratios': [1, 1, 1]})

# Remove the extra subplot in the third row
fig.delaxes(ax[2, 1])

# Flatten the subplots array for easier iteration
ax = ax.flatten()[:5]

# Loop through the subplots and plot data
for i in range(5):
    for j in range(len(range_change)):
        with open(hill_climbing_file[j][i], "rb") as file:
            ga = pickle.load(file)
        ax[i].plot(range(1, 10001), ga, label=f"range = {range_change[j]}")
    ax[i].set_title(f"N={range_N[i]}")
    ax[i].set_xlabel("Iteration")
    ax[i].set_ylabel("Best fitness")
    ax[i].legend()

# Adjust the spacing between the subplots
fig.tight_layout()


if __name__ == "__main__":
    # Display the figure
    plt.show()
