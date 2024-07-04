#load libraries
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#read data
airbnb = pd.read_csv('Airbnb_NYC_2019.csv')

#check top rows
airbnb.head()

#Count plot using matplot
vis1 = airbnb['neighbourhood_group'].value_counts().plot(kind='bar', title = 'Airbnb neighbourhood rooms in NY', figsize = (14,6))
vis1.set_xlabel('Neighbourhood')
vis1.set_ylabel('Number of rooms')
vis1.tick_params(axis='x', rotation=45)

#Count plot using seaborn
plt.figure(figsize=(14,8))
vis1 = sns.countplot(airbnb['neighbourhood_group'])
vis1.set(xlabel='Neighbourhood', ylabel='Number of rooms', title='Airbnb neighbourhood rooms in NY')
plt.show()

#scatter plot using matplot
plt.scatter(airbnb['neighbourhood_group'],airbnb['price'],color ='green')
plt.title('Room price in neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('Price')
plt.show()

#scatter plot using seaborn
plt.figure(figsize=(14,6))
vis1= sns.scatterplot(data = airbnb, x='neighbourhood_group', y='price', color = 'green')
vis1.set(xlabel='Neighbourhood', ylabel='Price', title='Room price in neighbourhood')
plt.show()

#adding hue & size
plt.figure(figsize=(14,6))
sns.scatterplot(data = airbnb, x='neighbourhood_group', y='price', hue= 'room_type')
vis1.set(xlabel='Neighbourhood', ylabel='Price', title='Room price in neighbourhood')
plt.show()

plt.figure(figsize=(14,6))
sns.scatterplot(data = airbnb, x='neighbourhood_group', y='price', hue= 'room_type', size='number_of_reviews')
vis1.set(xlabel='Neighbourhood', ylabel='Price', title='Room price in neighbourhood')
plt.show()

#plot geographical area using latitude & longitude
plt.figure(figsize=(14,6))
sns.scatterplot(data = airbnb, x='latitude', y='longitude', hue= 'neighbourhood_group')
plt.show()

#box plot 
plt.figure(figsize=(14,6))
sns.boxplot(data=airbnb,x='neighbourhood_group',y='availability_365' )
plt.show()