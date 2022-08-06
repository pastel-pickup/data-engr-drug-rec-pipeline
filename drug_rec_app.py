import sqlite3
conn = sqlite3.connect("drugdb.db")
c = conn.cursor()
execute(

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import inspect
import streamlit as st

data = pd.read_csv("C:/Users/New User/Desktop/top_drugs.csv")

condition = data.condition.unique()

st.title("PeopleRX: A Drug Recommendation System For People By The People")

st.header("This system recommends top 3 most effective medications for a chosen medical condition")

st.subheader("Enter a medical condition:")

st.selectbox("Condition", condition, index=1)

def drug_rec(user_condition):
    engine = create_engine("sqlite:///C:/Users/New User/Desktop/drugdb.db")
    drug_results = pd.read_sql('SELECT COUNT(*)OVER(PARTITION BY drugName) AS reviews, drugName, condition, rating, rank FROM drug_top WHERE condition= '+user_condition+' ORDER BY rating DESC;', engine)
    drug_results = drug_results.drop_duplicates()
    print(drug_results[:3])

if st.button("Recommend Me:"):
    drug_rec(condition)

st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")
