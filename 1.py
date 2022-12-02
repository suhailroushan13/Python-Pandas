# Python Pandas
# Python Data Analysis Library
# Pandas -  Panel Data
"""
Data Manipluation and Analysis
1.Data Series ==> 1D
2.Data Frames ==> Multi Dimensional
// Pandas is Built on Top of Numpy
"""
import pandas as pd
import numpy as np

print(pd.__version__)

a1 = pd.Series([1, 2, 3, 5, 6 ])
print(a1)

a2 = pd.Series([2,4,6,8,10])

# a2 = pd.Series({name: "Suhail", age: 20})

print(a1 + 10)
print(a1 - 10)

print(a1 * 10)

print(a1 / 10)

print(a1 % 10)

print('Vector')

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print(a1 % a2)
