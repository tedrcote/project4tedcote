import pandas as pd
import streamlit as st

data  = pd.read_csv("vehicles_us.csv")

st.write(data.head())
st.header ('Market for Used Vehicles. Analysis Tool.')