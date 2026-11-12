import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv("Advertising_F.csv")
st.title("Advertising Effectiveness Jackson Bowmer")

st.sidebar.head("Filters")
x_var=st.selectbox("X axis",["TV","radio","newspaper"])

#show scatterplot
fig=px.scatter(df, x=x_var,y="sales", labels={"TV": "Tv add spend", "radio":"Radio add spend"})

st.plotly_chart(fig)

#show the bar plot
sales_per_city=df.groupby("City")["sales"].sum().reset_index()
fig=px.bar(sales_per_city,x="City",y="sales",title="Data is fun")

st.plotly_chart(fig)

#show the data frame
st.dataframe(df)
