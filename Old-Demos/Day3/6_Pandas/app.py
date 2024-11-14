import pandas as pd
from matplotlib import pyplot as plt

# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }

# purchases = pd.DataFrame(data)
# purchases = pd.DataFrame(data, index=["Manish","Abhijeet","Ramakant","Pravin"])

# print(purchases)
# print(purchases.loc['Abhijeet'])
# print(purchases.describe())

# purchases.to_csv("purchases.csv")
# purchases.to_json("purchases.json")

# --------------------------------------------- Reading from CSV file

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

# print(movies_df)
# print(movies_df.head(2))
# print(movies_df.tail(2))
# print(movies_df.info())
# print(movies_df.shape)

# --------------------------------------------- Creating and Removing Duplicates

# temp_df = movies_df.append(movies_df)
# print(temp_df.shape)
# print(movies_df.shape)

# temp_df = temp_df.drop_duplicates()
# temp_df.drop_duplicates(inplace=True)

# temp_df.drop_duplicates(inplace=True, keep="first")  # Drop duplicates except for the first occurrence.
# temp_df.drop_duplicates(inplace=True, keep="last")  # Drop duplicates except for the last occurrence.
# temp_df.drop_duplicates(inplace=True, keep=False)  # Drop all duplicates

# print(temp_df.shape)

# ------------------------------------------ Column Processing

# print(movies_df.columns)

movies_df.rename(columns={
    'Runtime (Minutes)': 'Runtime',
    'Revenue (Millions)': 'Revenue_Millions'
}, inplace=True)

# movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year',
#        'runtime', 'rating', 'votes', 'revenue_millions',
#        'metascore']

movies_df.columns = [col.lower() for col in movies_df]

# print(movies_df.columns)

# ---------------------------------------------------- Work with missing values (Removing Data)
# print(movies_df.info())
# print(movies_df.isnull())
# print(movies_df.isnull().sum())

# temp_df = movies_df.dropna()
# print(temp_df.isnull().sum())
# print(temp_df.shape)

# movies_df.dropna(inplace=True)
# print(movies_df.isnull().sum())
# print(movies_df.shape)

# Remove Columns containing Null
# movies_df.dropna(inplace=True, axis=1)
# print(movies_df.isnull().sum())
# print(movies_df.shape)

# ---------------------------------------------------- Work with missing values (Imputation of Data)
revenue = movies_df['revenue_millions']
# print(revenue.head())
# print(revenue.shape)
# print(revenue.describe())

revenue_mean = revenue.mean()
# print(revenue_mean)

movies_df.fillna(revenue_mean, inplace=True)
# print(movies_df.isnull().sum())

# print(movies_df['genre'].describe())
# print(movies_df['genre'].value_counts())

# print(movies_df.corr())

# ---------------------------------------------- slicing, selecting, extracting
# genre_col = movies_df['genre']
# print(type(genre_col))

# genre_col = movies_df[['genre']]
# print(type(genre_col))

# subset = movies_df[['genre', 'rating']]
# print(subset)

# Data by Rows
# m = movies_df.loc["Prometheus"]
# print(m)
# print(type(m))

# m = movies_df.iloc[1]
# print(m)
# print(type(m))

# movies_subset = movies_df.loc["Prometheus":"Sing"]
# movies_subset = movies_df.iloc[1:4]
# print(movies_subset)

# Conditional Selection
# condition = (movies_df['director'] == 'Ridley Scott')
# print(condition)

# condition = movies_df[movies_df['director'] == 'Ridley Scott']
# print(condition)

# condition = movies_df[movies_df['rating'] > 8.6]
# print(condition)

# movies by Christopher Nolan OR Ridley Scott
# condition = movies_df[(movies_df['director'] == 'Ridley Scott') | (movies_df['director'] == 'Christopher Nolan')]
# condition = movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])]
# print(condition)


# we want all movies that were released between 2005 and 2010, have a rating above 8.0, but made below the 25 percentile in revenue

# condition = movies_df[
#     ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
#     & (movies_df['rating'] > 8.0)
#     & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))
# ]
# print(condition)

# ---------------------------------------------------------------- Apply Custom Functions
# def rating_fn(x):
#     if x >= 8.0:
#         return 'good'
#     else:
#         return 'bad'


# movies_df["rating_category"] = movies_df['rating'].apply(rating_fn)
# print(movies_df.head())

# movies_df["rating_category"] = movies_df['rating'].apply(
#     lambda x: 'good' if x >= 8.0 else 'bad')
# print(movies_df.head())

# ---------------------------------------------------------------- Plotting

# plt.bar(movies_df['rating'], movies_df['revenue_millions'])
# plt.scatter(movies_df['rating'], movies_df['revenue_millions'])

temp_df = movies_df[movies_df['director'] == 'Ridley Scott']
temp_df["rating_category"] = temp_df["rating"].apply(
    lambda x: 'good' if x >= 8.0 else 'bad')

# print(temp_df["rating_category"].value_counts())

fig1, ax1 = plt.subplots()
ax1.pie(temp_df["rating_category"].value_counts(), labels=[
        "Bad", "Good"], autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.show()
