import streamlit as  st
import numpy as np
import pandas as  pd


st.title("MTA Daily Ridership Analysis App", anchor=False)

df = pd.read_csv("MTA+Daily+Ridership/MTA_Daily_Ridership.csv")

with st.expander("MTA Daily Ridership Analysis DataFrame"):
    st.dataframe(df)


st.subheader("Share of traffic by service")
st.dataframe(pd.DataFrame({
    'Service': ['Subways', 'Buses', 'LIRR'],
    'Average Traffic': [
        df['Subways: Total Estimated Ridership'].mean(),
        df['Buses: Total Estimated Ridership'].mean(),
        df['LIRR: Total Estimated Ridership'].mean()
    ]
}).sort_values(by='Average Traffic', ascending=False))




st.subheader("Which service saw the biggest drop in traffic?")
st.dataframe(pd.DataFrame({
    'Service': ['Subways', 'Buses', 'LIRR'],
    'Average Recovery': [
        df['Subways: % of Comparable Pre-Pandemic Day'].mean(),
        df['Buses: % of Comparable Pre-Pandemic Day'].mean(),
        df['LIRR: % of Comparable Pre-Pandemic Day'].mean()
    ]
}).sort_values(by='Average Recovery'))






st.subheader("Which service was the fastest to recover?")
st.dataframe(pd.DataFrame({
    'Service': ['Subways', 'Buses', 'LIRR'],
    'Recovery': [
        df['Subways: % of Comparable Pre-Pandemic Day'].mean(),
        df['Buses: % of Comparable Pre-Pandemic Day'].mean(),
        df['LIRR: % of Comparable Pre-Pandemic Day'].mean()
    ]
}).sort_values(by='Recovery', ascending=False))




st.subheader("When will all services return to pre pandemic levels?")

latest = df.sort_values('Date').iloc[-1]

recovery = pd.DataFrame({
    'Service': ['Subways', 'Buses', 'LIRR'],
    'Latest Recovery': [
        latest['Subways: % of Comparable Pre-Pandemic Day'],
        latest['Buses: % of Comparable Pre-Pandemic Day'],
        latest['LIRR: % of Comparable Pre-Pandemic Day']
    ]
}).sort_values(by='Latest Recovery', ascending=False)

st.dataframe(recovery)