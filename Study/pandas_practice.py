"""
Description: A script to study and practice Pandas library.
Author: Kartikay Singh
Date: 2024-09-08
"""

import pandas as pd

# Create a DataFrame
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

mycars = pd.DataFrame(mydataset)
print(mycars)

# checking pandas version
print(f"The current version of pandas installed on this computer is: {pd.__version__}")