import pandas as pd
import numpy as np
from sqlalchemy import create_engine, exc
import streamlit as st

e = create_engine("sqlite:///C:\\Users\\New User\\Desktop\\drugdb.db")
c = e.connect()

try:
    # suppose the database has been restarted.
    c.execute(text("SELECT * FROM top_drugs"))
    c.close()
except exc.DBAPIError, e:
    # an exception is raised, Connection is invalidated.
    if e.connection_invalidated:
        print("Connection was invalidated!")

# after the invalidate event, a new connection
# starts with a new Pool
c = e.connect()
c.execute(text("SELECT * FROM top_drugs"))


data = pd.read_sql("SELECT * FROM top_drugs", con=e)

condition = data.condition.unique()

st.title("PeopleRX: A Drug Recommendation System For People By The People")

st.header("This system recommends top 3 most effective medications for a chosen medical condition")

st.subheader("Enter a medical condition:")

st.selectbox("Condition", condition, index=1)

if st.button("Recommend Me:"):
    drug_rec(condition)

st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")
