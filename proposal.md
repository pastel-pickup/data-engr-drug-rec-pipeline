# PeopleRX: A Drug Recommendation System For The People By The People
Mai Tran

# QUESTION/NEED:
# What is the end service that your project will provide? What is the purpose of the system you plan to build?
- End service of the project is to recommend top 3 most effective medications for a given medical condition inputted by end user. 
- This drug recommendation system serves as a clinical decision support (CDS) system to help both healthcare providers and patients to be more informed in choosing the most appropriate drugs for the patient's medical condition. This PeopleRX drug recommendation system will also serve as a backup reference to supplement the medical knowledge of the healthcare providers, and to help them make better decisions for their patients, allow them to spend more quality care time together, and to improve the overall care experience of the patient.

# Who is your client and how will that client benefits from your end service?
- My client is CVS, which is looking to provide more online healthcare services for its customers. Both of the healthcare providers as well as customers of CVS could benefit from this PeopleRX recommendation system to help them efficiently pick out drugs that are most suitable for their medical conditions while cutting down time and costs. 

# A preliminary diagram of end-to-end data pipeline of PeopleRX:
 <img width="750" alt="drug-rec-pipeline" src="https://user-images.githubusercontent.com/67651332/180668137-2fe89bf0-d7cc-494b-b9a6-76acf42cae5d.PNG">


# DATA DESCRIPTION:
# What dataset(s) do you plan to use, and how will you obtain the data? Please include a link! (The link can be to the dataset you’re downloading, the site you’re scraping, etc.)
- I am using a dataset of drug reviews from University of California Irvine Machine Learning Repository created by Surya Kallumadi and Felix Gräßer.
- https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29

# Do you plan to be able to automatically pull in new data at a regular cadence (e.g with Airflow or a cron job)?
- This dataset is no longer updated by their creators, so there will not be any new data pull from this dataset. 

# What is an individual sample/unit of analysis in this project? In other words, what does one row or observation of the data represent?
- An individual sample of analysis is as follows:
1. drugName (categorical): name of drug
2. condition (categorical): name of condition
3. review (text): patient review
4. rating (numerical): 10 star patient rating
5. date (date): date of review entry
6. usefulCount (numerical): number of users who found review useful

# What characteristics/features do you expect to work with? In other words, what are your columns of interest?
- My columns of interest are: 1) drugName, 2) condition, 3) review, 4) rating, and 6) usefulCount

# If modeling, what will you predict as your target?
- If modeling, either or a combination of positive drug reviews (text) and high rating (numerical) are my target.

# TOOLS:
- MongoDB - data storage
- Spark - data processing
- Airflow - data testing
- Streamlit - web depoyment

# MVP GOAL:
# What would a minimum viable product (MVP) look like for this project?
- data stored in MongoDB and processed in Spark
