# PeopleRX: A Drug Recommendation System For The People by The People
Mai Tran

# Abstract
Drug recommendation system, PeopleRX, serves as a clinical decision support (CDS) system to help both healthcare providers and patients to be more informed in choosing the most appropriate drugs for fast and efficient treatment without painful side effects, long wait time, uncertainty, human error, costs, and all other unpleasant experiences associated with long clinical drug trials. The recommender was successfully built using a data pipeline starting from a SQLite database, with data getting extracted and transformed via SQLAlchemy, and getting deployed to the web via Streamlit. 

# Design
1. Clean Data - The original dataset with 212,850 rows and 10 columns were cleaned by removing all columns except for 'drugName', 'condition', and 'rating'. Since there was no Natural Language Processing needed, the review column with text data was removed as well. Using 'rating' to rank the 'drugName' on a specific 'condition' was considered sufficient to build a recommender based on RANK() funcion in Structured Query Language (SQL). 

2. Explanatory Data Analysis (EDA) - With 212,850 rows of data, there were only 3,665 unique drug names in the dataset along with 916 different health conditions with a rating between 1-10. 

3. Storing Data In SQLite Database - To make the dataset compact and robust for web deployment in Streamlit, drugs with low ratings (less than 8) were removed, and only drugs with high ratings (8 or above) were kept in the dataset. A new column called "Reviews" was added to denote how many reviews were given for each drug. Duplicate rows were also removed. After this compact dataset was created, it was stored in a SQLite database. The resultant dataset was comprised of 128,451 rows with 4 columns. 

4. Building Recommender - To facilitate communication between data stored in SQLite database and recommender built in Python, SQLAlchemy was used to connect SQL language with Python language. In SQL language, the RANK(), COUNT()OVER(PARTITION BY), and ORDER BY functions were used to rank the best drugs for every condition in the dataset based on 'Rating' and 'Reviews'. The recommender code in Python was successfully built and was able to retrieve accurate recommended drugs for medical conditions such as "Acne", "Depression", "HIV Infection", and "Schizophrenia" as shown below:
  <img width="355" alt="drug_rec_python" src="https://user-images.githubusercontent.com/67651332/183768792-fba64425-ddae-4c90-a88c-74b75a937d9f.PNG">

5. Deploying Recommender Web-Application via Streamlit - 

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

