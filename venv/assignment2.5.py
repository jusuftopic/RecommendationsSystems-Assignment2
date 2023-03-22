import pandas as pd

ratings = pd.read_csv('ratings_small.csv', low_memory=False)
ratings_grouped = ratings.groupby(by='userId')

user_ids = list(ratings_grouped.groups.keys())

user_a_group = ratings_grouped.get_group(user_ids[0])
user_a_movies = set(user_a_group.movieId)

similar_users = set(user_a_group.userId)

for user_id in user_ids:
    user_movies = set(ratings_grouped.get_group(user_id).movieId)
    if len(user_a_movies.intersection(user_movies)) >= 3:
        similar_users.add(user_id)


print(similar_users)

