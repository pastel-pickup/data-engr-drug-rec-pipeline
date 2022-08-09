# PeopleRX: A Drug Recommendation System For The People by The People
Mai Tran

# Abstract
Drug recommendation system, PeopleRX, serves as a clinical decision support (CDS) system to help both healthcare providers and patients to be more informed in choosing the most appropriate drugs for fast and efficient treatment without painful side effects, long wait time, uncertainty, human error, costs, and all other unpleasant experiences associated with long clinical drug trials. The recommender was successfully built using a data pipeline starting from a SQLite database, with data getting extracted and transformed via SQLAlchemy, and getting deployed to the web via Streamlit. 

# Design
1. Clean Data - The original dataset with 212,850 rows and 10 columns were cleaned by removing all columns except for 'drugName', 'condition', and 'rating'. Since there was no Natural Language Processing needed, the review column with text data was removed as well. Using 'rating' to rank the 'drugName' on a specific 'condition' was deemed sufficient to build a recommender based solely on RANK() funcion in Structured Query Language (SQL). 
2. Explanatory Data Analysis (EDA) - 
3. Building & Testing Recommender -
4. Storing Data In SQLite Database - 
5. Building & Testing Web-Application in Streamlit -

# Data
- The dataset of drug reviews from University of California Irvine Machine Learning Repository was created by Surya Kallumadi and Felix Gräßer.
- Here is the link to the dataset: https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29
- Each row of the dataset is made of the following features or columns:
1. drugName (categorical): name of drug
2. condition (categorical): name of condition
3. review (text): patient review
4. rating (numerical): 10 star patient rating
5. date (date): date of review entry
6. usefulCount (numerical): number of users who found review useful
-
-
-

# Algorithms 

# Tools
- Numpy and Pandas for data manipulation
- Regular Expressions for text cleaning
- SQLite for data storage
- Streamlit for data processing & web deployment

# Communication
This is a Graphical User Interface (GUI) of a web-based application of the PeopleRX Recommendation System built in Streamlit:
![image](https://user-images.githubusercontent.com/67651332/183754647-a6ad7995-d514-4f13-8123-18a1a4374e57.png)

