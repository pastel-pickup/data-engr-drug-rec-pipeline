import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import pymysql



engine = sqlalchemy.create_engine(
    "mssql+pyodbc://DESKTOP-H9GNET5/New User:M4iSQLServer@DESKTOP-H9GNET5/mydb?driver=ODBC+Driver+17+for+SQL+Server", 
    )

conn = engine.connect()

data = pd.read_sql('SELECT * mytable;', conn)

st.write(data)
