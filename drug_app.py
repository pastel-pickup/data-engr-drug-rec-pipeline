import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import pymysql

#creating connection

@st.cache(allow_output_mutation=True)
def get_connection():
    return create_engine("mssql+pyodbc://username:M4iSQLServer@DESKTOP-H9GNET5/mydb?driver=ODBC+Driver+17+for+SQL+Server", 
    fast_executemany = True
    )

data = pd.read_sql('SELECT * FROM mytable', engine)

st.write(data)
