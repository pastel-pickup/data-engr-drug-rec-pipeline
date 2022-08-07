import pandas as pd
import numpy as np
from sqlalchemy import create_engine, MetaData, text
import streamlit as st

engine = create_engine('sqlite:///data/drugdb.db', echo=True)

meta = MetaData()

tq = text("SELECT * FROM top_drugs")
conn = engine.connect()
result = conn.execute(tq).fetchall()
st.write(result)
