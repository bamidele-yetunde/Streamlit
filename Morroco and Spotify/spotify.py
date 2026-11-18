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
        st.subheader("Platform Pie Chart")
        platform_counts = df["platform"].value_counts()
        st.write(platform_counts)
        st.write(platform_counts.plot.pie(autopct="%1.1f%%", figsize=(5, 5)))

with album:
    st.subheader("Top 10 Albums by Stream Count")
    st.dataframe(df["album_name"].value_counts().head(10))


with artist:

    pass

with track:
    pass
