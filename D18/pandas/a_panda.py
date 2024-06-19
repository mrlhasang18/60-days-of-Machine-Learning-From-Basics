print("\n---- working with data : Statistics with NumPy -----\n")

'''
Pandas: Fast and Efficient DataFrame object for data manipulation.
It is powerful python data analysis toolkit, library.
Reading and writing datastructures and data formats: csv,tsv,XML,txt,JSON,etc.
'''

import pandas as pd
import os

# Check if the file exists in the current working directory
if os.path.exists("Private_data.csv"):
    # Create a DataFrame from a CSV file in the same folder
    a = pd.read_csv("Private_data.csv")
    # Read the DataFrame using the head() function
    print(a.head())
else:
    print("Error: The specified CSV file does not exist.")