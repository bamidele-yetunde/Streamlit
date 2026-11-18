import streamlit as  st
import numpy as np
import pandas as  pd

# name = ['John', 'Alice', 'Bob']
# age = [25, 30, 22]

# my_name = np.array(name)
# my_age = np.array(age)




# st.write('My name is:', my_name)

# st.write('My age is:', my_age)


# person = [['John', 'Alice', 'Bob'], [25, 30, 22]]

# full_info = pd.DataFrame(person, index=["Name", "Age"], columns=["Person 1", "Person 2", "Person 3"])

# st.write("Full Information Dataframe:")
# st.dataframe(full_info)



import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.title("My Spotify Streaming History Analysis App", anchor=False)

df = pd.read_csv("spotify_history.csv")

# TS COLUMN
df["ts"] = pd.to_datetime(df["ts"])
df["year"] = df["ts"].dt.year
df["month"] = df["ts"].dt.month
df["month_name"] = df["ts"].dt.month_name()
df["quarter"] = df["ts"].dt.quarter
df["day"] = df["ts"].dt.day
df["hour"] = df["ts"].dt.hour
df["second"] = df["ts"].dt.second
with st.expander("Show Spotify Streaming History DataFrame"):
    st.dataframe(df)


col1, col2 , col3, col4, col5= st.columns(5)

# col1.metric("Total Streams", df.shape[0])
with col1:
    st.markdown("**Total Streams**")
    st.write(df.shape[0])
with col2:
    st.markdown("Unique Songs")
    st.write(df["track_name"].nunique())

with col3:
    st.markdown("Unique platform")
    st.write(df["platform"].nunique())

with col4:
    st.markdown("Unique Artists")
    st.write(df["artist_name"].nunique())

with col5: 
    st.markdown("Unique Albums")
    st.write(df["album_name"].nunique())


platfrom, album, artist, track= st.tabs(["Platform", "Album_name", "Artist_name", "Track_name"])

with platfrom:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Platform Analysis")
        platform_counts = df["platform"].value_counts()
        st.bar_chart(platform_counts)
    with col2:
        st.subheader("Platform Chart")
        platform_counts = df["platform"].value_counts()
        st.write(platform_counts)
        st.write(platform_counts.plot.pie(autopct="%1.1f%%", figsize=(5, 5)))

with album:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Top 10 Albums by Stream Count")
        st.dataframe(df["album_name"].value_counts().head(10))

    with col2:
        st.subheader('Top 10 Artists by Album Count')
        st.dataframe(df.groupby('artist_name') ['album_name'].nunique().sort_values(ascending=False).head(10))


with artist:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Top 10 Album Name')
        st.dataframe(df.groupby('album_name') ['track_name'].nunique().sort_values(ascending=False).head(10))

    with col2:
        st.subheader('Top 10 Artists')
        st.dataframe(df['artist_name'].value_counts().head(10))     

with track:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Top 10 Track Name')
        st.dataframe(df['track_name'].value_counts().head(10)) 

    with col2:
        st.subheader('Bottom 10 Track Name')
        st.dataframe(df['track_name'].value_counts().tail(10)) 



# TAB 2

year, month, quarter, day= st.tabs(["Year", "Month", "Quarter", "Day"])

with year:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Number of Streams Per Year')
        st.dataframe(df.groupby('year').size().sort_values(ascending=False))

    with col2:
        st.subheader('Total Listening Time Per Year')
        st.dataframe(df.groupby('year')['ms_played'].sum().sort_values(ascending=False))


with month:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Number of Streams Per Month')
        st.dataframe(df.groupby('month_name').size().sort_values(ascending=False))

    with col2:
        st.subheader('Total Listening Time Per Month')
        st.dataframe(df.groupby('month_name')['ms_played'].sum().sort_values(ascending=False))




with quarter:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Number of Streams Per Quarter')
        st.dataframe(df.groupby('quarter').size().sort_values(ascending=False))

    with col2:
        st.subheader('Total Listening Time Per Month')
        st.dataframe( df.groupby('quarter')['ms_played'].sum().sort_values(ascending=False))




with day:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Number of Streams Per Day')
        st.dataframe(df.groupby('day').size().sort_values(ascending=False))

    with col2:
        st.subheader('Total Listening Time Per Day')
        st.dataframe( df.groupby('day')['ms_played'].sum().sort_values(ascending=False))