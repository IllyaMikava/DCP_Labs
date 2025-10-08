import pandas as pd 

df = pd.read_csv("album.csv")

# 1. how many alums in data set
print("Number of albums:", df.shape[0])

# 2. what are collum names
print("\nColumn names:" )
for c in df.columns:
    print(c)

# 3. which artists appear in the first five albums?
print("\nFrist 5 artists:" )
print(df.head(5)['artist'])

# 4. which artists appear in the last five albums?
print("\nlast 5 artists")
print(df.tail(5)['artist'])

#5. What data type is each column?
print("\ndatatypes info:")
print(df.dtypes)

#6. Are there any missing values??
print('\nmissing values')
print(df.isnull().sum())

# 7. How many unique artists are in the dataset?
num_artists = df['artist'].nunique()
print("\nNumber of unique artists:", num_artists)

# 8. who are the artists?
unique_artists = df['artist'].unique()
print("\nList of unique artists:")
print(unique_artists)




# 2.1 Load and Inspect Tracks
df2 = pd.read_csv("albumtracktune.csv")

num_tracks = df2.shape[0]
print("\nNumber of tracks in the dataset:", num_tracks)

# What columns does this dataset have?
print("Column names in the dataset:")
print(df2.columns)

# the albumtracktune.csv file has a foreign key relationship with album.csv through the album_id column.

# 2.2: Track Numbers
highest_track_number = df2['track_num'].max()
print("\nHighest track number on any album:", highest_track_number)

max_tunes_in_track = df2['tune_num'].max()
print("\nMaximum number of tunes in a single track:", max_tunes_in_track)

# Display the most frequent tune titles
tune_counts = df2['title'].value_counts()
print("\nMost frequent tune titles across all albums:")
print(tune_counts.head(10))  



# Task 3.1: Albums by Artist

print("\nTask 3.1\n")

# 1. Albums by "Altan"
altan_albums = df[df['artist'] == 'Altan']
print("Albums by Altan:")
print(altan_albums)
print("Number of albums by Altan:", altan_albums.shape[0], "\n")

# 2. Albums by "Martin Hayes"
martin_albums = df[df['artist'] == 'Martin Hayes']
print("Albums by Martin Hayes:")
print(martin_albums)
print("Number of albums by Martin Hayes:", martin_albums.shape[0], "\n")

# 3. Albums by "The Bothy Band"
bothy_albums = df[df['artist'] == 'The Bothy Band']
print("Albums by The Bothy Band:")
print(bothy_albums)
print("Number of albums by The Bothy Band:", bothy_albums.shape[0])


print("\nTask 3.2\n")

# 1. Find all tracks on album_id 1
album1_tracks = df2[df2['album_id'] == 1]
print("Tracks on album_id 1:")
print(album1_tracks)


num_tracks = album1_tracks['track_num'].nunique()
print("\nNumber of tracks on album_id 1:", num_tracks)


total_tunes = album1_tracks['tune_num'].sum()
print("Total number of tunes on album_id 1:", total_tunes)


print("\nTask 4.1\n")

# 1. Group tracks by album_id and count how many tracks each album has
tracks_per_album = df2.groupby('album_id')['track_num'].nunique()
print("Number of tracks per album:")
print(tracks_per_album)

# 2. Find which album has the most tracks
max_tracks = tracks_per_album.max()
album_most_tracks = tracks_per_album[tracks_per_album == max_tracks]
print("\nAlbum(s) with the most tracks:")
print(album_most_tracks)

