import pandas as pd

TITLE_KEY = 'title'
POPULARITY_KEY = 'popularity'

data = [['Toy Story', 21.946943],['Jumanji', 17.015539],['Grumpier Old Men', 11.7129]]
dataframe = pd.DataFrame({
     TITLE_KEY: ['Toy Story', 'Jumanji', 'Grumpier Old Men'],
     POPULARITY_KEY: [21.946943, 17.015539, 11.7129]})
dataframe_sorted = dataframe.sort_values(by=POPULARITY_KEY, ascending=True)
print(dataframe_sorted[POPULARITY_KEY])