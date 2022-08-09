import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development


st.set_page_config(
    page_title="Top Drugs Data Dashboard",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_url = "https://raw.githubusercontent.com/pastel-pickup/data-engr-drug-rec-pipeline/main/top_drugs.csv"

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
     return pd.read_csv(dataset_url)

df = get_data()

# dashboard title
st.title("PeopleRX: Top Drugs Recommender")

# top-level filters
condition_filter = st.selectbox("Select the Condition", pd.unique(df["condition"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["condition"] == condition_filter]

st.markdown("### Detailed Data View")
st.dataframe(df.drop_duplicates())



