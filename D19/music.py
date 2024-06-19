# Lets's create a custom data(csv file) for music recommendation model


import pandas as pd
import random

# Let's define lists to store random values
ages = [random.randint(18, 65) for _ in range(100)]
genders = [1 if random.random() < 0.5 else 0 for _ in range(100)]
genres = [random.choice(["Rock", "Pop", "Jazz", "Classical", "Hip-Hop"]) for _ in range(100)]

# dictionary with the random values
m = {"age": ages, "gender": genders, "genre": genres}

# DataFrame from the dictionary
df = pd.DataFrame(m)

# Now creating a CSV file from the DataFrame df
df.to_csv("music_recommendation.csv", index=False)