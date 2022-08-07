import sqlite3
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, text
import streamlit as st

engine = create_engine("sqlite:///C:\\Users\\New User\\Desktop\\drugdb.db", echo=False)

meta = MetaData()

tq = text("SELECT * FROM top_drugs")
conn = engine.connect()
result = conn.execute(tq).fetchall()
st.write(result)
