#load library
import pandas as pd

#load data source
data = pd.read_csv(r"C:\Users\ADHIRAJ MAJUMDAR\Documents\simplilearn data science assignment\tableau 10\corona\31st March data set.csv")

#Groupping Country Region
dataAverage = data.groupby("Country_Region").sum().reset_index()

#changing Active status
dataAverage["New Active"] =dataAverage["Confirmed"] - dataAverage["Deaths"] - dataAverage["Recovered"]
del dataAverage["Active"]
dataAverage["Active"] = dataAverage["New Active"]
del dataAverage["New Active"]

#take output file
dataAverage.to_excel(r"C:\Users\ADHIRAJ MAJUMDAR\Documents\simplilearn data science assignment\tableau 10\corona\31st March final data set.xlsx",index=False)