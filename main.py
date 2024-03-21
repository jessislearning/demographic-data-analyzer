# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
import pandas as pd
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)


## -------my code is here----------
#df=pd.read_csv("adult.data.csv")
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
#higher_education_rich = len(higher_education[higher_education["salary"]==">50K"])/len(higher_education)#round(len(higher_education[higher_education["salary"] == ">50K"])/len(higher_education)*100,2)
#higher_education_rich = round(len(higher_education[df.salary == ">50K"].value_counts())/len(higher_education)*100, 1)
#lower_education_rich = round(len(lower_education[lower_education["salary"] == ">50K"])/len(lower_education)*100,2)
#print (round(len(df[higher_education])/len(df)*100, 2)) #percentage of higher education grads over df
#print (len(higher_education[higher_education["salary"]==">50K"]))
#print (lower_education_rich)

#min number of hours per week, and how many are rich - working
#min_work_hours = df["hours-per-week"].min()
#min_workers = df[df["hours-per-week"] == min_work_hours]
#num_min_workers = len(min_workers)
#rich_percentage = round(len(min_workers[min_workers["salary"]==">50K"])/len(min_workers)*100, 2)
#print (num_min_workers)
#print (rich_percentage)

#Which country has the highest percentage of people who are rich
#countries = df[df["salary"] == ">50K"].groupby("native-country").count()/df.groupby("native-country").count()
#print (countries.sort_values("salary", ascending=False).index[0])
#countries = df[df["salary"] == ">50K"]["native-country"].value_counts()/df["native-country"].value_counts()
#print (countries.sort_values(ascending=False).index[0])

#rich_per_country = df[df["salary"] == ">50K"]["native-country"].value_counts()/df["native-country"].value_counts()
#highest_earning_country = rich_per_country.idxmax()
#highest_earning_country_percentage = round(len(df[df["salary"]==">50K"][df["native-country"]==highest_earning_country])/len(df[df["native-country"]==highest_earning_country])*100, 2)
#print(highest_earning_country_percentage)

#top_IN_occupation = df[df["native-country"]== "India"][df["salary"]==">50K"]["occupation"].value_counts()
#print(top_IN_occupation.idxmax())
