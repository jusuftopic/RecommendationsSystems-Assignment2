import pandas as pd

ratings = pd.read_csv('ratings_small.csv', low_memory=False)
ratings_grouped = ratings.groupby(by='movieId')
ratings_calculations = ratings_grouped['rating'].agg(['mean', 'median'])
ratings_list = []

for id, row in ratings_calculations.iterrows():
    ratings_list.append({'id': id, 'mean': row['mean'], 'median': row['median']})

print(ratings_list)

