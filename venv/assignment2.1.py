import pandas as pd

data = ['Toy Story','Jumanji','Grumpier Old Men']

#print first element
print(data[0])
#print first two element
print(data[:2])
#print last two elements
print(data[1:3])

data_series = pd.Series(data=data, index=['a', 'b', 'c'], name='data_series')
print(data_series['b'])

