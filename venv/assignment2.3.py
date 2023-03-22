import numpy
import pandas as pd

# constants
RELEASE_DATE_KEY = 'release_date'
RELEASE_YEAR_KEY = 'release_year'

movies = pd.read_csv('movies_metadata.csv', low_memory=False)

#first and last movie
print(movies.iloc[0])
print(movies.iloc[-1])

# Information about the movie 'Jumanji'
print(movies[movies['original_title'] == 'Jumanji'])

def to_float(x):
 try:
     x = float(x)
 except:
     x = numpy.nan
 return x

movies_small_df = movies[['title', 'release_date', 'popularity', 'revenue','runtime', 'genres']].copy()
movies_small_df.loc[RELEASE_DATE_KEY] = pd.to_datetime(movies_small_df[RELEASE_DATE_KEY], errors='coerce')
movies_small_df[RELEASE_YEAR_KEY] = movies_small_df[RELEASE_DATE_KEY].apply(
    lambda x: str(x).split('-')[0] if x != numpy.nan else numpy.nan)
movies_small_df[RELEASE_YEAR_KEY] = movies_small_df[RELEASE_YEAR_KEY].apply(to_float)
movies_small_df[RELEASE_YEAR_KEY] = movies_small_df[RELEASE_YEAR_KEY].astype('float')

print(movies_small_df[movies_small_df[RELEASE_YEAR_KEY] > 2010])