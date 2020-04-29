import pandas as pd
import matplotlib.pyplot as plt

#LOADING THE DATA-------- (how will this be different using database?)
#had to download the file and copy the path
iris = pd.read_csv('/Users/martinvazquez/Downloads/iris/Iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

#JUST LIKE R
#print(iris.head())

wine_reviews = pd.read_csv('/Users/martinvazquez/Downloads/wine-reviews/winemag-data-130k-v2.csv', index_col=0)
#print(wine_reviews.head())

#using matplotlib-----------------------------------
# create a figure and axis
fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])

#set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

fig.show()
