# PredPol---Crime-Analysis
Crimes have been severely increased in past few years, the Problem Statement includes analysis of crimes with different perspectives including utmost attributes possible and predicting via the study of nature of crimes committed. Predictions will be made to provide local authorities with an upper hand on crime and help them plan a better strategy to tackle the same. Dataset Source: https//: data.gov.in and https://data.org, 2017 Dataset for crimes committed.

Dataset is contained in "dataset.csv" file. It is preprocessed data and ready to use.
Time Mapper : "time_mapper.py" file is the program that takes dataset file as input by reading it line by line and passes only the required data from each data (tuple/row) to the "time_reducer.py" file.
Time Reducer : Here crime type along with its time of occurence is received as input from the mapper file and all the crimes types are calculated for each time-phase. Here I have divided 24 hours time period into 8 parts of 3 hours each.

Location Mapper : Here crime spot's LATITUDE & LONGITUDE values are passed to the "location_reducer.py" file and locations are manually divided into 8 sections based on LATITUDE values range.
Location Reducer : It does the same work as Time Reducer but in this case for location based.

Location Cluster : "location_cluster.py" file is a reducer file which groups together the crimes into clusters which are closer to each other using K-means clustering algorithm.

HOW TO RUN : I used VMWare platform for Linux based platform to run the program. But it can be run directly on python IDLE too.

=> For time :
cat dataset.csv|./time_mapper.py|./time_reducer.py

=> For Location :
cat dataset.csv|./location_mapper.py|./location_reducer.py

=> For Location Cluster :
cat dataset.csv|./location_mapper.py|./location_cluster.py
