# PeopleRX Drug Recommender
Mai Tran

# Minimum Viable Product (MVP)

The goal of this project is to build a scalable web application of a drug recommender called PeopleRX.
  1. I successfully set up an EC2 instance on AWS and installed both Anaconda and MongoDB via the command line
  2. I succesfully imported JSON data into MongoDB and retrieved the said data
  3. I successfully built the web interface of the drug recommender using Streamlit. The web interface looks as follows:
 <img width="383" alt="streamlit_app" src="https://user-images.githubusercontent.com/67651332/182268852-ae1a3335-c86d-4649-a7c9-070cba9dbeb3.png">

For next steps, I will:
  1. Convert my NLP dataset in CSV to JSON, and have it imported into MongoDB
  2. Look into AWS Comprehend Medical for Medical NLP processing, to see if my NLP model can be integrated there
  3. Look into integration between AWS and Streamlit throught AWS SDK for Python (Boto3)
