# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
import pandas as pd
from unittest import main

# Test your function by calling it here
#demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
#main(module='test_module', exit=False)


## -------my code is here----------
df=pd.read_csv("adult.data.csv")
#male- working
#print (df["sex"].value_counts())
#df_male = df[df["sex"]=="Male"]
#print(df["education"].unique())
#print (df_male["age"].mean())
#print (df.groupby(["race"]).count())#
#print (df.pd.series.groupby(["race"]).count())

#print % of bachelors - working
#percentage_bachelors = round(len(df[df["education"]=="Bachelors"])/len(df)*100, 2)
#print(percentage_bachelors)

#print % of higher education rich - working
#higher_education = df[df["education"].isin(["Bachelors","Masters","Doctorate"])]
#lower_education = df[~df["education"].isin(["Bachelors","Masters","Doctorate"])]
#higher_education_rich = round(len(higher_education[higher_education["salary"] == ">50K"])/len(higher_education)*100)
#lower_education_rich = round(len(lower_education[lower_education["salary"] == ">50K"])/len(lower_education)*100)
#print (round(len(df[higher_education])/len(df)*100, 2)) #percentage of higher education grads over df
#print (higher_education_rich)
#print (lower_education_rich)
