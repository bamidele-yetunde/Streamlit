import numpy as np
import pandas as pd
import streamlit as st


st.title("Power Consumption Analysis", anchor=False)

df = pd.read_csv("powerconsumption.csv")
with st.expander("Power Consumption Analysis DataFrame"):
    st.dataframe(df)



# st.write(df)


# Prepare the data
df["Datetime"] = pd.to_datetime(df["Datetime"])
df["Total"] = df["PowerConsumption_Zone1"] + df["PowerConsumption_Zone2"] + df["PowerConsumption_Zone3"]
df["Hour"] = df["Datetime"].dt.hour
df["Day"] = df["Datetime"].dt.day_name()
df["Month"] = df["Datetime"].dt.month


# Q1
st.header("Q1: Seasonal Patterns")
st.write("What seasonal patterns occur in electricity consumption at the hourly, weekly, and annual levels?")

st.subheader("Hourly")
hourly = df.groupby("Hour")["Total"].mean()
st.write(hourly.sort_values(ascending=False))
st.line_chart(hourly)
st.write("Highest hour:", hourly.idxmax())
st.write("Lowest hour:", hourly.idxmin())

st.subheader("Weekly")
weekly = df.groupby("Day")["Total"].mean().sort_values(ascending=False)
st.write(weekly)
st.bar_chart(weekly, sort=False)

st.subheader("Annual")
monthly = df.groupby("Month")["Total"].mean()
st.write(monthly.sort_values(ascending=False))
st.bar_chart(monthly)
st.write("Highest month:", monthly.idxmax())
st.write("Lowest month:", monthly.idxmin())

st.write("**Findings:** Electricity use is lowest around 6 AM and peaks around 8 PM. "
         "Sunday has the lowest use. July and August are the highest months, likely because of "
         "air conditioning in summer, and December is the lowest.")


# Q2
st.header("Q2: Weather and Electricity Use")
st.write("Are temperature, wind speed, and humidity correlated with electricity consumption? "
         "Which has the strongest relationship?")

correlation = df[["Temperature", "Humidity", "WindSpeed", "Total"]].corr()["Total"].sort_values(ascending=False)
st.write(correlation)

st.write("**Findings:** Temperature has the strongest relationship (0.49). When it gets hotter, "
         "electricity use goes up. Humidity (-0.30) and wind speed (0.22) have weak relationships.")


# Q3
st.header("Q3: Zone Differences")
st.write("Do different zones have different patterns in electricity consumption?")

zones = ["PowerConsumption_Zone1", "PowerConsumption_Zone2", "PowerConsumption_Zone3"]

st.subheader("Share of Total Power (%)")
st.write((df[zones].sum() / df[zones].sum().sum() * 100).sort_values(ascending=False))

st.subheader("Each Zone by Month")
zone_monthly = df.groupby("Month")[zones].mean()
st.write(zone_monthly)
st.line_chart(zone_monthly)
st.write("Busiest month for each zone:", zone_monthly.idxmax())

st.subheader("Each Zone by Hour")
zone_hourly = df.groupby("Hour")[zones].mean()
st.line_chart(zone_hourly)
st.write("Busiest hour for each zone:", zone_hourly.idxmax())

st.write("**Findings:** Zone 1 uses the most power (about 45%). All zones peak around 8 PM, "
         "but their yearly patterns differ. Zone 1 is steady, Zone 2 rises in winter, "
         "and Zone 3 jumps sharply in summer.")
