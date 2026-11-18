import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px



if "raw_df" not in st.session_state:
    st.session_state.raw_df = pd.read_csv("powerconsumption.csv")

df = st.session_state.raw_df.copy()

# df = pd.read_csv("powerconsumption.csv")

# ploty visulization

df["PowerConsumption_all"] = df["PowerConsumption_Zone1"] + df["PowerConsumption_Zone2"] + df["PowerConsumption_Zone3"]
df["Datetime"] = pd.to_datetime(df["Datetime"])
df["year"] = df["Datetime"].dt.year
df["month"] = df["Datetime"].dt.month
df["day"] = df["Datetime"].dt.day
df["day_name"] = df["Datetime"].dt.day_name()
df["month_name"] = df["Datetime"].dt.month_name()

# Bar chart of electricity consumption month

fig = px.bar(df, x="month_name", y="PowerConsumption_all", color="year", barmode="group", title="Electricity Consumption by Month")
st.plotly_chart(fig)


# pie chart of electricity consumption by day of the week
fig2 = px.pie(df, names="day_name", values="PowerConsumption_all", title="Electricity Consumption by Day of the Week")
st.plotly_chart(fig2, use_container_width=True)


# line chart of electricity consumption by day
fig = px.line(df, x="Datetime", y="PowerConsumption_all", title="Electricity Consumption by Day")
st.plotly_chart(fig, use_container_width=True)


# df_days_consump = 
st.write(df.groupby(["day_name"])["PowerConsumption_all"].sum().reset_index())
fig = px.line(df.groupby(["day_name"])["PowerConsumption_all"].sum().reset_index(), x="day_name", y="PowerConsumption_all", title="Electricity Consumption by Day of the Month")
st.plotly_chart(fig, use_container_width=True)


# donut
# histogram
# slicer
# heatmap
# scatter

fig = px.scatter(
    df,
    x="Temperature",
    y="PowerConsumption_all",
    hover_data=["Datetime"],
    opacity=0.6,
    title="Total Power Consumption vs. Temperature"
)

# 3. Display the chart
st.plotly_chart(fig, use_container_width=True)





zone_totals = pd.DataFrame({
    "Zone": ["Zone 1", "Zone 2", "Zone 3"],
    "Total Power": [
        df["PowerConsumption_Zone1"].sum(),
        df["PowerConsumption_Zone2"].sum(),
        df["PowerConsumption_Zone3"].sum()
    ]
})

fig_donut = px.pie(
    zone_totals,
    names="Zone",
    values="Total Power",
    hole=0.4,  # This turns the pie chart into a donut chart
    title="Power Consumption Share by Zone"
)
st.plotly_chart(fig_donut, use_container_width=True)




# histogram
fig_hist = px.histogram(
    df,
    x="PowerConsumption_all",
    nbins=30,
    title="Distribution of Total Power Consumption"
)
st.plotly_chart(fig_hist, use_container_width=True)





# slicer
temp = st.slider("Temperature Range:", float(df["Temperature"].min()), float(df["Temperature"].max()), (10.0, 30.0))
df = df[df["Temperature"].between(temp[0], temp[1])]




# heatmap
cols = ["Temperature", "Humidity", "WindSpeed", "GeneralDiffuseFlows", "DiffuseFlows", "PowerConsumption_all"]
corr = df[cols].corr()

fig_heatmap = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap: Weather vs. Power Consumption"
)
st.plotly_chart(fig_heatmap, use_container_width=True)








