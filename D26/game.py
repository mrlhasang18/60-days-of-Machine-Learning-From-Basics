import numpy as np
'''
So for this simple game we are going to use 2 sub-package in numpy:
seed(): sets the random seed, so that your results are reproducible between simulations.
        As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
rand(): if you don't specify any arguments, it generates a random float between zero and one.
'''
np.random.seed(123)
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5:
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print("Dice: ",dice)
print("Step: ",step)

# head tails game
print("------ Head or Tails ---------")
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)


# Random walk

# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()

# Distribution

final_tails = []
for x in range(10000):
    tails = [0]
    for x in range(10):
        coin =  np.random.randint(0,2)
        tails.append(tails[x]+ coin)
    final_tails.append(tails[-1])
print(final_tails)

# all this values represents distribution

plt.hist(final_tails,bins =10)
plt.show()