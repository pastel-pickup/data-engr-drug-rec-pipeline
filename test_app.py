import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3 as sqlite
import streamlit as st

engine = create_engine("sqlite:///C:\\Users\\New User\\Desktop\\drugdb.db")
con = engine.connect()

data = pd.read_sql("SELECT * FROM top_drugs")

condition = data.condition.unique()

st.title("PeopleRX: A Drug Recommendation System For People By The People")

st.header("This system recommends top 3 most effective medications for a chosen medical condition")

st.subheader("Enter a medical condition:")

st.selectbox("Condition", condition, index=1)

if st.button("Recommend Me:"):
    drug_rec(condition)

st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")
