import streamlit as st
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import pymysql

#creating connection

e = create_engine("mssql+pyodbc://DESKTOP-H9GNET5/New User:M4iSQLServer@DESKTOP-H9GNET5:1433/mydb?driver=ODBC+Driver+17+for+SQL+Server&Connect+Timeout=30")

print(e.dialect.create_connect_args(e.url))
