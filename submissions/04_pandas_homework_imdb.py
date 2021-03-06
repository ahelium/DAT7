'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''
import pandas as pd
# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')
# check the number of rows and columns
movies.shape
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.duration.mean()
# sort the DataFrame by duration to find the shortest and longest movies
movies.duration.order
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

# convert the following content ratings to "NC-17": X, TV-MA

# count the number of missing values in each column

# if there are missing values: examine them, then fill them in with "reasonable" values

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours

# calculate the average duration for each genre

'''
ADVANCED LEVEL
'''

# check if there are multiple movies with the same title, and if so, determine if they are the same movie

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
