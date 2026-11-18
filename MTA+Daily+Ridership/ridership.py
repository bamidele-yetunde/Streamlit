import numpy as np
import pandas as pd
import streamlit as st

df = pd.read_csv("MTA+Daily+Ridership/MTA_Daily_Ridership.csv")


st.header("Subways: Total Estimated Ridership")
st.write("What was the share of traffic by service before the pandemic? Did it change?")

du_pandemic= df[(df["Date"] >= "2020-03-01") &  (df["Date"] <= "2021-06-30")]

st.write("Total Estimated Ridership")
st.write( df["Subways: Total Estimated Ridership"].sum())

st.write("Subways: Total Estimated Ridership During Pandemic")

st.write((du_pandemic["Subways: Total Estimated Ridership"].sum()/ df["Subways: Total Estimated Ridership"].sum()) * 100)
