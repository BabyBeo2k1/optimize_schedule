import matplotlib.pyplot as plt
import pickle


range_N = [10, 50, 100, 150, 200]
GA_file = [f"record_{N}_{1000}.pickle" for N in range_N]
hill_climbing_file = [f"record_{N}_{2}.pickle" for N in range_N]

# Create the figure and the subplots
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 10), gridspec_kw={'width_ratios': [1, 1], 'height_ratios': [1, 1, 1]})

# Remove the extra subplot in the third row
fig.delaxes(ax[2, 1])

# Flatten the subplots array for easier iteration
ax = ax.flatten()[:5]

# Loop through the subplots and plot data
for i in range(5):
    print(GA_file[i])
    with open(GA_file[i], "rb") as file:
        ga = pickle.load(file)
    with open(hill_climbing_file[i], "rb") as file:
        hill_climbing = pickle.load(file)
    ax[i].plot(range(1, 10001), ga, label="GA")
    ax[i].plot(range(1, 10001), hill_climbing, label="Hill climbing")
    ax[i].set_title(f"N={range_N[i]}")
    ax[i].set_xlabel("Iteration/Generation")
    ax[i].set_ylabel("Best fitness")
    ax[i].legend()

# Adjust the spacing between the subplots
fig.tight_layout()


if __name__ == "__main__":
    # Display the figure
    plt.show()
