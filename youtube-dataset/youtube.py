import pandas as pd

# https://www.kaggle.com/datasets/samithsachidanandan/most-popular-1000-youtube-videos/data
df = pd.read_csv('yt-1000.csv')

print(df)

print(df.head())  # By default, shows the first 5 rows

print(df.describe())

# Remove commas from numbers for numeric sorting
df['Video views'] = df['Video views'].str.replace(',', '').astype(float)
df['Likes'] = df['Likes'].str.replace(',', '').astype(float)
df['Dislikes'] = df['Dislikes'].str.replace(',', '').astype(float)

print("")
print("")
print("TOP TEN LIKES")
print(df.nlargest(10, 'Likes'))

print("")
print("")
print("TOP TEN DISLIKES")
print(df.nlargest(10, 'Dislikes'))

print("")
print("")
print("TOP TEN VIEWS")
print(df.nlargest(10, 'Video views'))
