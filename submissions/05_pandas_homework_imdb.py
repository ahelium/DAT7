'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns
movies.describe()
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')

# create a histogram of duration, choosing an "appropriate" number of bins
#this is throwing an error, possibly bcause of the version of pandas I am using. I upgrated but no change.
movies.duration.plot(kind='hist', bins=3)
# this works
movies.duration.hist(bins=50)
# use a box plot to display that same data
movies.boxplot(column='duration')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
plt.xlabel('content_rating')
plt.ylabel('# ratings')
plt.title('movie ratings')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
content = set(movies.content_rating)

movies.content_rating.replace(['NOT RATED', 'APPROVED','PASSED','GP'],'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X', 'TV-MA'],'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()       # count the missing values in each column

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
movies.content_rating.fillna(value='PG', inplace=True)
movies['content_rating'][movies.title == 'True Grit'] = 'PG-13'

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies['star_rating'][movies.duration <= 120].mean()

# use a visualization to detect whether there is a relationship between star rating and duration
movies.plot(kind='scatter',x='star_rating', y='duration')
# calculate the average duration for each genre

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

movies.duration.hist(by=movies.content_rating, sharex=True, sharey=True)

# determine the top rated movie (by star rating) for each genre
movies.groupby('genre').star_rating.max()

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.duplicated('title')]

# calculate the average star rating for each genre, but only include genres with at least 10 movies
movies.groupby('genre').star_rating.mean()[movies.genre.value_counts() >= 10]

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
