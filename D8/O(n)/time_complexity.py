# Let's calculate the time complexity
import time

def calculate_time_complexity(n):
    start_time = time.time()

    # Simulate some computation that takes O(n^2) time
    for i in range(n):
        for j in range(n):
            # Do some dummy computation
            result = i * j

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time

# Test the function with different input sizes
n_values = [100, 200, 400, 800, 1600]
for n in n_values:
    execution_time = calculate_time_complexity(n)
    print(f"n={n}, execution time={execution_time:.2f} seconds")

# Plot the results to visualize the time complexity
import matplotlib.pyplot as plt

n_values = [100, 200, 400, 800, 1600]
execution_times = [calculate_time_complexity(n) for n in n_values]

plt.plot(n_values, execution_times)
plt.xlabel("Input size (n)")
plt.ylabel("Execution time (seconds)")
plt.title("Time complexity of the algorithm")
plt.show()