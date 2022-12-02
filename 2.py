import pandas as pd
import numpy as np
# data1 = [1,3,5,7,9]
# data2 = [2,4,6,7,9]
# b1 = pd.Series(data1)
# b2 = pd.Series(data2)
# print(b1 == b2)

# data1 = {names:'Suhail',age:20}
# data2 = {names:"Roushan",age:20}
# obj1 = pd.Series(data1)
# obj2 = pd.Series(data2)
# print(obj1 == obj2)

a = np.arange(5)
index = ['a','f','d','e',"h"]
a = pd.Series(a,index);
a.reset_index()