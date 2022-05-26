from ast import increment_lineno
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('books.csv', engine = 'python')
#print out the first 10 rows of data
print(df.head(n=10))
#the column headers
print(df.columns)
#the header data types
print(df.dtypes)
#descriptive statistics
print(df.describe())

#making a plot graphing average rating versus number of pages
avgRate = df['average_rating']
numPage = df['num_pages']
plt.scatter(avgRate, numPage)
plt.xlabel('Average Rating')
plt.ylabel('Number of Pages')
plt.show()


