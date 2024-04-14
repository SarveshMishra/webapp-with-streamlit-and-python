import streamlit as st
import pandas as pd
import numpy as np

DATE_URL = (
    "/home/sarvesh/repo/webapp-with-streamlit-and-python/Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Motor_Vehicle_Collisions in NYC")
st.markdown(
    "This application is a Streamlit dashboard that can analyse motor vehicle collison in NYC")


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATE_URL, nrows=nrows, parse_dates=[
                       ['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data


data = load_data(100000)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider(
    "Number of persons injured in vehicle collison", 0, 19)

st.map(data.query("injured_persons >= @injured_people")
       [['latitude', 'longitude']].dropna(how="any"))

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)
