import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, text
import streamlit as st
from sqlalchemy.sql import select

engine = create_engine("sqlite:///C:\\Users\\New User\\Desktop\\drugdb.db", echo=False)

data = pd.read_sql("SELECT * FROM top_drugs ORDER BY reviews, rating;", con=engine)



condition = data.condition.unique()

st.title("PeopleRX: A Drug Recommendation System For People By The People")
st.header("This system recommends top 3 most effective medications for a chosen medical condition")

st.write(data.drop_duplicates())

st.subheader("Enter a medical condition:")

st.selectbox("Condition", condition, index=1)

@st.cache
def drug_rec(condition):
 tq = text("SELECT * FROM top_drugs WHERE condition = "+condition+"ORDER BY reviews, rating DESC LIMIT 3;")
 conn = engine.connect()
 result = conn.execute(tq).fetchall()
 return result

if st.button("Recommend Me:"):
    drug_rec(condition)

meta = MetaData()



st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")


